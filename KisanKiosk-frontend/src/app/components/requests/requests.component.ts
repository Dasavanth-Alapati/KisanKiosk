import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-requests',
  templateUrl: './requests.component.html',
  styleUrls: ['./requests.component.css']
})
export class RequestsComponent implements OnInit {
  reqs:any;
  request:any = {
    decision:false,
    id:'',
    user:this.base.id(),
  }
  constructor(private api:ApiService,private base:BaseService) { }

  ngOnInit(): void {
    this.api.fetchRequests().subscribe(data => {
      this.reqs = data;
    })
  }
  roleaction(id:string,decision:boolean){
    this.request.decision = decision;
    this.request.id = id;
    this.api.requestApproval(this.request).subscribe();
    window.location.reload();
  }

}
