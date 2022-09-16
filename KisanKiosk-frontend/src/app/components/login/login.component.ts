import { Component, OnInit } from '@angular/core';
import { ApiService } from 'src/app/services/api-service.service';
import { loginModel } from 'src/app/models/loginModel';
import { Router } from '@angular/router';
import { CookieService } from 'ngx-cookie-service';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { catchError, throwError } from 'rxjs';
import { HttpErrorResponse } from '@angular/common/http';


@Component({
  selector: 'app-login',
  templateUrl: './login.component.html',
  styleUrls: ['./login.component.css']
})
export class LoginComponent implements OnInit {

  loginform !: FormGroup;
  clicked = false;
  unauth = false;
  constructor(private apiservice: ApiService, private router: Router, private form: FormBuilder) { }

  ngOnInit(): void {
    this.loginform = this.form.group({
      username: ['', Validators.required],
      password: ['', Validators.required],
    })
  }
  login() {
    if (this.loginform.invalid) {
      this.clicked = true;
      return;
    }
    let credentials: loginModel = {
      username: this.loginform.controls['username'].value,
      password: this.loginform.controls['password'].value,
    }

    this.apiservice.apilogin(credentials).subscribe({
      next: (data) => {
        localStorage.setItem('token', JSON.stringify(data));
        this.apiservice.fetchProfile().subscribe(data => {
          sessionStorage.setItem('user', JSON.stringify(data));
        })
        this.router.navigate(['']);
      },
      error:(err:HttpErrorResponse) => {
        if (err.status == 401) this.unauth = true;
      },
    });
    }
}
