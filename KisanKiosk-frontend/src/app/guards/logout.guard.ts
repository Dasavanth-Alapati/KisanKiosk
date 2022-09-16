import { Location } from '@angular/common';
import { Injectable } from '@angular/core';
import { ActivatedRouteSnapshot, CanActivate, RouterStateSnapshot, UrlTree } from '@angular/router';
import { Observable } from 'rxjs';
import { BaseService } from '../services/base.service';

@Injectable({
  providedIn: 'root'
})
export class LogoutGuard implements CanActivate {

  constructor(private base: BaseService,private location:Location){}
  canActivate(
    route: ActivatedRouteSnapshot,
    state: RouterStateSnapshot): Observable<boolean | UrlTree> | Promise<boolean | UrlTree> | boolean | UrlTree {
      if (this.base.loggedIn()){
        if(confirm('Already logged in, Do you want to log out?'))
        this.base.logout('login');
        else
        this.location.back();
      }
    return !this.base.loggedIn();
  }
  
}
