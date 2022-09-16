import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-marketplace',
  templateUrl: './marketplace.component.html',
  styleUrls: ['./marketplace.component.css']
})
export class MarketplaceComponent implements OnInit {
  products: any;
  constructor(private api: ApiService, public base: BaseService, private router: Router) { }

  ngOnInit(): void {
    if (this.base.loggedIn())
    this.api.fetchMarket().subscribe(data => {
      this.products = data;
    })
  }
}
