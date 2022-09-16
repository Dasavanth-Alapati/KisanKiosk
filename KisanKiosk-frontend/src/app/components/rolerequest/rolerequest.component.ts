import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-rolerequest',
  templateUrl: './rolerequest.component.html',
  styleUrls: ['./rolerequest.component.css']
})
export class RolerequestComponent implements OnInit {
  rolerequest:any = {
    role:'',
    reason:'',
    user:this.base.id(),
  };
  constructor(private router:Router,private route:ActivatedRoute,private base:BaseService,private api:ApiService) { }

  ngOnInit(): void {
    this.rolerequest.role = this.route.snapshot.params['role'];
  }

  submit(){
    this.rolerequest.user = this.base.id()
    this.api.createRequest(this.rolerequest).subscribe();
    this.router.navigate(['']);
  }

}
