import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-comment',
  templateUrl: './comment.component.html',
  styleUrls: ['./comment.component.css']
})
export class CommentComponent implements OnInit {

  id:any;
  comment:any;
  constructor(private api:ApiService,private route:ActivatedRoute,public base:BaseService) { }

  ngOnInit(): void {
    this.id = this.route.snapshot.params['id'];
    this.api.fetchComment(this.id).subscribe(data => {
      this.comment = data;
    })
  }

}
