import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-myorders',
  templateUrl: './myorders.component.html',
  styleUrls: ['./myorders.component.css']
})
export class MyordersComponent implements OnInit {
  orders:any;
  constructor(private api:ApiService,public base:BaseService) { }

  ngOnInit(): void {
    this.api.fetchMyOrders(this.base.id()).subscribe(data => {
      this.orders = data;
    })
  }

}
