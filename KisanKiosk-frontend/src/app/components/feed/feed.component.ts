import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-feed',
  templateUrl: './feed.component.html',
  styleUrls: ['./feed.component.css']
})
export class FeedComponent implements OnInit {
  posts:any;
  constructor(private api:ApiService,public base:BaseService) { }

  ngOnInit(): void {
    if (this.base.loggedIn())
    this.api.fetchFeed().subscribe(data => {
      this.posts =data;
    })
  }

}
