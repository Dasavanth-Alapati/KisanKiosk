import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';
import { Location } from '@angular/common';
import { order } from 'src/app/models/orderModel';

@Component({
  selector: 'app-order',
  templateUrl: './order.component.html',
  styleUrls: ['./order.component.css']
})
export class OrderComponent implements OnInit {
  listing: any;
  profile: any;
  order:order = {
    user:this.base.id(),
    order:'',
    status:'ORDERED',
  }
  constructor(private route: ActivatedRoute, private api: ApiService, private base: BaseService,private router:Router,private location:Location) { }

  ngOnInit(): void {
    let id = this.route.snapshot.params['id'];
    this.api.fetchListing(id).subscribe(data => {
      this.listing = data;
    })
    this.base.profileDetails.subscribe(data => {
      this.profile = data;
    })
  }
  confirm(): void {
    this.order.order = this.listing.id;
    this.api.startOrder(this.order).subscribe();
    this.location.back();
  }
  cancel(): void {
    this.location.back();
  }
}
