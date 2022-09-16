import { Component, OnInit } from '@angular/core';
import { AsyncValidatorFn, FormBuilder, FormGroup, Validators } from '@angular/forms';
import { Router } from '@angular/router';
import { catchError, map, Observable, take } from 'rxjs';
import { loginModel } from 'src/app/models/loginModel';
import { signupModel } from 'src/app/models/signupModel';
import { ApiService } from 'src/app/services/api-service.service';

@Component({
  selector: 'app-sign-up',
  templateUrl: './sign-up.component.html',
  styleUrls: ['./sign-up.component.css']
})
export class SignUpComponent implements OnInit {


  Signup!:FormGroup;
  clicked = false;

  constructor(private fb:FormBuilder,private api:ApiService,private router:Router) { }

  ngOnInit(): void {
    this.Signup = this.fb.group({
      username:['',{validators:[Validators.required,Validators.minLength(5),],asyncValidators:this.checkUsername(),updateOn:'blur'}],
      password:['',Validators.required],
      name:['',[Validators.required,Validators.minLength(5),]],
      role:['Farmer'],
    })

  }
  signup(){
    this.clicked = true
    if(this.Signup.invalid){
      return
    }
    let signupdata:signupModel = {
      username:this.Signup.controls['username'].value,
      password:this.Signup.controls['password'].value,
      name:this.Signup.controls['name'].value,
      role:this.Signup.controls['role'].value,
    }
    this.api.signUp(signupdata).subscribe(data =>{
      let login:loginModel = {
        username:this.Signup.controls['username'].value,
        password:this.Signup.controls['password'].value,
      }
      this.api.apilogin(login).subscribe(data => {
        localStorage.setItem('token',JSON.stringify(data));
        this.api.fetchProfile().subscribe(data => {
        sessionStorage.setItem('user',JSON.stringify(data));
        if (signupdata.role == 'Farmer')
        this.router.navigate(['']);
        else
        this.router.navigate(['rolerequest/'+signupdata.role]);
        })
      })
    });
  }

  checkUsername():AsyncValidatorFn{
    return (control):Observable<any> =>{
      const username = control.value
    return this.api.checkUsername(username).pipe(take(1),
      map(res => res.exists ? {'alreadyExists': true} : null)
    );
  }}
}
