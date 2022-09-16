export interface signupModel{
    username:string;
    password:string;
    name:string;
    role:'Admin'|'Expert'|'Vendor'|'Farmer';
}