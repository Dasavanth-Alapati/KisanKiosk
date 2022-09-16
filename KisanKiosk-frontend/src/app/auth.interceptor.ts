import { Injectable } from '@angular/core';
import {
  HttpRequest,
  HttpHandler,
  HttpEvent,
  HttpInterceptor,
  HttpErrorResponse,
  HttpClient
} from '@angular/common/http';
import { catchError, Observable, switchMap, throwError } from 'rxjs';
import { BaseService } from './services/base.service';

@Injectable()
export class AuthInterceptor implements HttpInterceptor {


  constructor(private base:BaseService,private http: HttpClient,) {}
  refresh = false;
  static token:any;
  intercept(request: HttpRequest<unknown>, next: HttpHandler): Observable<HttpEvent<unknown>> {
    if(AuthInterceptor.token = this.base.fetchToken())
    request = request.clone({
      setHeaders:{
        Authorization: `Bearer ${AuthInterceptor.token.access}`
      }
    })
    return next.handle(request).pipe(
      catchError((err: HttpErrorResponse) => {
        if(err.status === 401 && !this.refresh){
        this.refresh = true;
        if (this.base.loggedIn()){
        return this.http.post('http://localhost:8000/api/token/refresh/', {'refresh':AuthInterceptor.token.refresh}, {withCredentials: true}).pipe(
          switchMap((res:any) => {
            AuthInterceptor.token.access = res['access'];
            localStorage.setItem('token', JSON.stringify(AuthInterceptor.token));
            return next.handle(request.clone({
              setHeaders: {
                Authorization: `Bearer ${AuthInterceptor.token.access}`
              }
            }));
          })
        ).pipe(catchError((err:HttpErrorResponse)=> {
          if(err.status === 401)
          localStorage.clear();
          return throwError(() => err);
        }));
      }}
      this.refresh = false;
      return throwError(() => err);
    }));;
  }
}
