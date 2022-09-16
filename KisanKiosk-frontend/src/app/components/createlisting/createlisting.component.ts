import { Component, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { listing } from 'src/app/models/listingModel';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-createlisting',
  templateUrl: './createlisting.component.html',
  styleUrls: ['./createlisting.component.css']
})
export class CreatelistingComponent implements OnInit {

  listing:listing = {
    name:'',
    description:'',
    price:0,
    user:this.base.id(),
  }
  listingform !:FormGroup; 
  constructor(private base:BaseService,private api:ApiService,private router:Router,private formbuilder:FormBuilder) { }

  ngOnInit(): void {
    this.listingform = this.formbuilder.group({
      name:['',Validators.required],
      description:[''],
      price:[1,[Validators.required,Validators.min(1)]]
    })
  }

  createlisting():void{
    if(this.listingform.invalid)return;
    let listing = this.listingform.value;
    listing.user = this.base.id();
    console.log(listing);
    this.api.createListing(listing).subscribe();
    this.router.navigate(['marketplace']);
  }
}
