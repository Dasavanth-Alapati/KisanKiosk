import { Location } from '@angular/common';
import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-editprofile',
  templateUrl: './editprofile.component.html',
  styleUrls: ['./editprofile.component.css']
})
export class EditprofileComponent implements OnInit {
  edit: any = {
    name: '',
    bio: '',
    role: '',
    user: this.base.id(),
  }


  constructor(public location: Location, private api: ApiService, private router: Router, private base: BaseService) { }

  ngOnInit(): void {
  }

  submit() {
    let role:string = '';
    if (this.edit.role != '' && this.edit.role != 'Farmer') {
      console.log('rolerequest/' + this.edit.role);
      role = this.edit.role
      this.router.navigate(['rolerequest/' + role]);
      console.log(this.edit.role);
      this.edit.role = '';
    }
    this.api.editProfile(this.edit).subscribe();
    if(role == 'Farmer' || role == '')this.router.navigate(['profile']);
  }

}
