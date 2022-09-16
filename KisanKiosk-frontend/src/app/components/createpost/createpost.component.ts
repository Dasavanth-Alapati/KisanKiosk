import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { post } from 'src/app/models/postModel';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-createpost',
  templateUrl: './createpost.component.html',
  styleUrls: ['./createpost.component.css']
})
export class CreatepostComponent implements OnInit {

  post:post={
    title:'',
    content:'',
    user:this.base.id(),
  }
  constructor(private base:BaseService,private api:ApiService,private router:Router) { }

  ngOnInit(): void {
  }

  createpost():void{
    if (this.post.title == '')return;
    this.api.createPost(this.post).subscribe();
    this.router.navigate(['feed']);
  }
}
