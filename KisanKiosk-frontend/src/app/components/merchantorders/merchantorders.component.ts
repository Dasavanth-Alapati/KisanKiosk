import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-merchantorders',
  templateUrl: './merchantorders.component.html',
  styleUrls: ['./merchantorders.component.css']
})
export class MerchantordersComponent implements OnInit {
  orders:any;
  status:string = '';
  constructor(private api:ApiService,public base:BaseService) { }

  ngOnInit(): void {
    this.api.fetchMerchantOrders(this.base.id()).subscribe(data => {
      this.orders = data;
    })
  }

}
