import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-listing',
  templateUrl: './listing.component.html',
  styleUrls: ['./listing.component.css']
})
export class ListingComponent implements OnInit {
  listing:any;
  id:any;
  constructor(private api:ApiService,private route:ActivatedRoute,public base:BaseService) { }

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];
    this.api.fetchListing(this.id).subscribe(data => {
      this.listing = data;
    })
  }

}
