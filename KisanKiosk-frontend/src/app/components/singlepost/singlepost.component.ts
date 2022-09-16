import { Component, OnInit } from '@angular/core';
import { ActivatedRoute, Router } from '@angular/router';
import { ApiService } from 'src/app/services/api-service.service';
import { BaseService } from 'src/app/services/base.service';

@Component({
  selector: 'app-singlepost',
  templateUrl: './singlepost.component.html',
  styleUrls: ['./singlepost.component.css']
})
export class SinglepostComponent implements OnInit {
  post: any;
  id: any;
  constructor(private router: ActivatedRoute, private api: ApiService,public base:BaseService) { }

  ngOnInit(): void {
    this.id = this.router.snapshot.params['id'];
    this.api.fetchSinglePost(this.id).subscribe(data => {
      this.post = data;
    })
  }
}
