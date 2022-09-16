import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { ApiService } from './api-service.service';
import * as moment from 'moment';
import { Router } from '@angular/router';
import { order } from '../models/orderModel';

@Injectable({
  providedIn: 'root'
})
export class BaseService {

  constructor(private apiservice: ApiService,private router:Router) { }
  profileDetails = new Observable((observer) => {
    let user: any = null;
    if(this.loggedIn()){
    if(user = sessionStorage.getItem('user')){
      user = JSON.parse(user);
    }
    else{
      this.apiservice.fetchProfile().subscribe(data => {
        sessionStorage.setItem('user',JSON.stringify(data));
        user = data;
        })
    }
  }
    if (user) {
      observer.next(user);
      observer.complete();
    }
    observer.next(null);
  }
  )

  pic(): string {
    let pic: string = 'default';
    this.profileDetails.subscribe({
      next: (profile: any) => {
        if (profile) {
          if (profile.profilepic) {
            pic = profile.credid.username;
          }
          else {
            pic = 'default';
          }
        }
        else {
          pic = 'default';
        }
      },
      complete: () => {
      }
    })
    return this.apiservice.baseurl + 'media/ProfilePics/' + pic + '.jpeg';
  }

  loggedIn(): boolean {
    let loggedin: boolean = false;
    if (this.fetchToken())loggedin = true;
    return loggedin;
  }

  role(): string | boolean {
    let role = '';
    this.profileDetails.subscribe({
      next: (profile: any) => {
        if (profile) {
          role = profile.role;
        }
        else {
          role = '';
        }
      },
      complete: () => {
      }
    })
    return role;
  }

  id(): string {
    let id = '';
    this.profileDetails.subscribe({
      next: (profile: any) => {
        if (profile) {
          id = profile.id;
        }
      }
    })
    return id;
  }
  age(time:string):string{
    return moment(time).fromNow();
  }

  order(listingid: any): void {
    this.router.navigate(['order/' + listingid]);
  }
  
  orderUpdate(id:string,status:string):void{
    if(status != ''){
      let order:order = {
        order:id,
        status:status,
      };
      this.apiservice.updateOrder(order).subscribe();
      window.location.reload();}
  }
  fetchToken(){
    let token:any = localStorage.getItem('token');
    if(token != null){
      token = JSON.parse(token);
      return token;}
    else return false;
  }

  logout(route:string = ''){
    localStorage.clear()
    sessionStorage.clear()
    this.router.navigate([route])
  }
}
