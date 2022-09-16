import { Component, OnInit, SimpleChanges } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-nav-bar',
  templateUrl: './nav-bar.component.html',
  styleUrls: ['./nav-bar.component.css']
})
export class NavBarComponent implements OnInit {

  constructor(public baseservice:BaseService,public apiservice:ApiService,private router:Router) { }

  ngOnInit(): void {
  }

  
}
