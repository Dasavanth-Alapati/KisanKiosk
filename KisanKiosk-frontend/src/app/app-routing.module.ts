import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { AddMoneyComponent } from './components/add-money/add-money.component';
import { CommentComponent } from './components/comment/comment.component';
import { CreatelistingComponent } from './components/createlisting/createlisting.component';
import { CreatepostComponent } from './components/createpost/createpost.component';
import { EditprofileComponent } from './components/editprofile/editprofile.component';
import { FeedComponent } from './components/feed/feed.component';
import { ListingComponent } from './components/listing/listing.component';
import { LoginComponent } from './components/login/login.component';
import { MarketplaceComponent } from './components/marketplace/marketplace.component';
import { MerchantordersComponent } from './components/merchantorders/merchantorders.component';
import { MyordersComponent } from './components/myorders/myorders.component';
import { OrderComponent } from './components/order/order.component';
import { ProfileComponent } from './components/profile/profile.component';
import { RequestsComponent } from './components/requests/requests.component';
import { RolerequestComponent } from './components/rolerequest/rolerequest.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { SinglepostComponent } from './components/singlepost/singlepost.component';
import { AuthGuard } from './guards/auth.guard';
import { LogoutGuard } from './guards/logout.guard';
import { RoleGuard } from './guards/role.guard';

const routes: Routes = [
  {path:'login',component:LoginComponent,canActivate:[LogoutGuard]},
  {path:'signup',component:SignUpComponent,canActivate:[LogoutGuard]},
  {path:'profile',component:ProfileComponent,canActivate:[AuthGuard]},
  {path:'profile/:id',component:ProfileComponent,canActivate:[AuthGuard]},
  {path:'marketplace',component:MarketplaceComponent},
  {path:'feed',component:FeedComponent},
  {path:'requests',component:RequestsComponent,canActivate:[AuthGuard,RoleGuard],data:{roles:['Admin']}},
  {path:'myorders',component:MyordersComponent,canActivate:[AuthGuard]},
  {path:'merchantorders',component:MerchantordersComponent,canActivate:[AuthGuard,RoleGuard],data:{roles:['Vendor']}},
  {path:'feed/post/:id',component:SinglepostComponent,pathMatch:'full',canActivate:[AuthGuard]},
  {path:'comment/:id',component:CommentComponent,canActivate:[AuthGuard]},
  {path:'marketplace/listing/:id',component:ListingComponent,pathMatch:'full',canActivate:[AuthGuard]},
  {path:'createpost',component:CreatepostComponent,canActivate:[AuthGuard]},
  {path:'createlisting',component:CreatelistingComponent,canActivate:[AuthGuard,RoleGuard],data:{roles:['Vendor']}},
  {path:'order/:id',component:OrderComponent,pathMatch:'full',canActivate:[AuthGuard]},
  {path:'addmoney',component:AddMoneyComponent,canActivate:[AuthGuard]},
  {path:'rolerequest/:role',component:RolerequestComponent,canActivate:[AuthGuard]},
  {path:'editprofile',component:EditprofileComponent,canActivate:[AuthGuard]},
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
