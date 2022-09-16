import { Component, EventEmitter, Input, OnInit, Output } from '@angular/core';
import { BaseService } from 'src/app/services/base.service';
import { LikeModel } from 'src/app/models/likeModel';
import { ApiService } from 'src/app/services/api-service.service';
import { comment } from 'src/app/models/commentModel';



@Component({
  selector: 'app-interactions',
  templateUrl: './interactions.component.html',
  styleUrls: ['./interactions.component.css']
})
export class InteractionsComponent implements OnInit {
  @Input() object: any = '';
  @Input() type = '';
 isActive = false;
  @Output() reload = new EventEmitter();
  status = 0;
  like = '/assets/images/like.png';
  dislike = '/assets/images/dislike.png';
  comment: comment = {
    comment: '',
    user: this.base.id(),
    id: '',
    type: '',
  }

  constructor(public base: BaseService, private api: ApiService) { }

  ngOnInit(): void {
    this.status = this.checklike();
    this.set();
  }

  set(): void {
    if (this.status == 1) {
      this.like = '/assets/images/liked.png'
      this.dislike = '/assets/images/dislike.png'
    }
    else if (this.status == -1) {
      this.like = '/assets/images/like.png'
      this.dislike = '/assets/images/disliked.png'
    }
    else if (this.status == 0) {
      this.like = '/assets/images/like.png'
      this.dislike = '/assets/images/dislike.png'
    }
  }

  checklike(): any {
    for (let i = 0; i < this.object.like.likeinfo.length; i++) {
      const element = this.object.like.likeinfo[i];
      if (element.profileid.id == this.base.id()) {
        if (element.likes == "YES") return 1;
        else if (element.likes == "NO") return -1;
        else return 0;
      }
    }
    return 0;
  }
  reset(data: any): void {
    if (this.status == data) {
      this.status = 0;
      if (data == 1) this.object.like.like--;
      else this.object.like.dislike--;
    }
    else {
      if (data == 1) {
        this.object.like.like++;
        if (this.status == -1) this.object.like.dislike--;
      }
      else {
        this.object.like.dislike++;
        if (this.status == 1) this.object.like.like--;
      }
      this.status = data;
    }
    this.set();
    let likedata: LikeModel = {
      like: this.object.like.id,
      status: this.status,
      user: this.base.id(),
    }
    this.api.like(likedata).subscribe();
  }

  commentsubmit(): void {
    if(this.comment.comment == '') return
    this.comment.type = this.type;
    this.comment.id = this.object.id;
    this.api.submitComment(this.comment).subscribe(() => {
      this.reload.emit();
    });
    this.comment.comment = '';
  }
}
