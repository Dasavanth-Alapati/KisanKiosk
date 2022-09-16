import { Injectable } from '@angular/core';
import { Observable } from 'rxjs';
import { loginModel } from '../models/loginModel';
import { HttpClient, HttpParams } from '@angular/common/http';

@Injectable({
  providedIn: 'root'
})
export class ApiService {
  baseurl = 'http://localhost:8000/'
  constructor(private http: HttpClient) { }
  //Login api
  apilogin(credentials: loginModel): Observable<any> {
    return this.http.post(this.baseurl + 'api/token/', credentials,{withCredentials:true});
  }

  fetchProfile(token: any = null): Observable<any> {
    if (token!= null){
    let params: HttpParams
    params = new HttpParams().set('token', token)
    return this.http.get(this.baseurl + 'profile/apiprofile/', { params: params });}
    else{
      return this.http.get(this.baseurl + 'profile/apiprofile/');}
    }
  
  // api for signup
  signUp(data: any): Observable<any> {
    return this.http.post(this.baseurl + 'apiregister/', data);
  }
  //api for fetching product listings
  fetchMarket(): Observable<any> {
    return this.http.get(this.baseurl + 'marketplace/apimarketplace/');
  }

  fetchFeed(): Observable<any> {
    return this.http.get(this.baseurl + 'posts/apifeed/');
  }

  fetchRequests(): Observable<any> {
    return this.http.get(this.baseurl + 'role/api/');
  }

  fetchMyOrders(id: string): Observable<any> {
    let params: any
    params = new HttpParams().set('id', id);
    return this.http.get(this.baseurl + 'order/apimyorders/', { params: params });
  }

  fetchMerchantOrders(id: string): Observable<any> {
    let params = new HttpParams().set('id', id);
    return this.http.get(this.baseurl + 'order/apimerchantorders/', { params: params });
  }

  fetchSinglePost(id: string): Observable<any> {
    let params = new HttpParams().set('id', id);
    return this.http.get(this.baseurl + 'posts/apipost/', { params: params });
  }

  fetchComment(id: string): Observable<any> {
    let params = new HttpParams().set('id', id);
    return this.http.get(this.baseurl + 'comments/apicomment/', { params: params });
  }

  fetchListing(id: string): Observable<any> {
    let params = new HttpParams().set('id', id);
    return this.http.get(this.baseurl + 'marketplace/apilisting/', { params: params });

  }
  like(data: any): Observable<any> {
    return this.http.post(this.baseurl + 'likes/apilike/', data);
  }
  submitComment(data: any): Observable<any> {
    return this.http.post(this.baseurl + 'comments/apicomment/', data);
  }
  createPost(data: any): Observable<any> {
    return this.http.post(this.baseurl + 'posts/apipost/', data);
  }
  createListing(data: any): Observable<any> {
    return this.http.post(this.baseurl + 'marketplace/apilisting/', data);
  }

  startOrder(data: any): Observable<any> {
    return this.http.post(this.baseurl + 'order/apiorder/', data);
  }

  updateOrder(data: any): Observable<any> {
    return this.http.put(this.baseurl + 'order/apiorder/', data);
  }

  addMoney(data: any): Observable<any> {
    return this.http.post(this.baseurl + 'profile/apimoney/', data);
  }

  requestApproval(data:any):Observable<any>{
    return this.http.put(this.baseurl + 'role/api/',data);
  }
  createRequest(data:any):Observable<any>{
    return this.http.post(this.baseurl + 'role/api/',data);
  }

  editProfile(data:any):Observable<any>{
    return this.http.put(this.baseurl + 'profile/apiprofile/',data)
  }

  checkUsername(data:any):Observable<any>{
    let params = new HttpParams().set('username', data);
    return this.http.get(this.baseurl + 'apiregister/',{ params: params })
  }
}
