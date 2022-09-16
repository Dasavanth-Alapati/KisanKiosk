import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-add-money',
  templateUrl: './add-money.component.html',
  styleUrls: ['./add-money.component.css']
})
export class AddMoneyComponent implements OnInit {
  money:any = {
    money:0,
    user:this.base.id(),
  };
  constructor(public base:BaseService,public location:Location,private api:ApiService) { }

  ngOnInit(): void {
  }
  add(){
    console.log(this.money);
    this.api.addMoney(this.money).subscribe();

    this.location.back();
  }
}
