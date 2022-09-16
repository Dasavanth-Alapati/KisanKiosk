import { Location } from '@angular/common';
import { Component, Input, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';


@Component({
  selector: 'app-profile',
  templateUrl: './profile.component.html',
  styleUrls: ['./profile.component.css']
})
export class ProfileComponent implements OnInit {
  profile:any;
  pic:any;

  constructor(public base:BaseService,private api:ApiService,private route:ActivatedRoute,public location:Location) { }

  ngOnInit(): void {
    let id:any = null;
    if(!(id = this.route.snapshot.params['id'])){
      id = this.base.id();
    }
    this.api.fetchProfile(id).subscribe(data =>{
      this.profile = data;
      if(this.profile.profilepic){
        this.pic = this.profile.credid.username;
      }
      else{
        this.pic = 'default';
      }
      this.pic = this.api.baseurl + 'media/ProfilePics/'+this.pic+'.jpeg';
    })
  }


}
