import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { ReactiveFormsModule } from '@angular/forms';
import { FormsModule } from '@angular/forms';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavBarComponent } from './components/nav-bar/nav-bar.component';
import { BaseComponent } from './components/base/base.component';
import { FeedComponent } from './components/feed/feed.component';
import { MarketplaceComponent } from './components/marketplace/marketplace.component';
import { ProfileComponent } from './components/profile/profile.component';
import { LoginComponent } from './components/login/login.component';
import { SignUpComponent } from './components/sign-up/sign-up.component';
import { HttpClientModule, HTTP_INTERCEPTORS } from '@angular/common/http';
import { RequestsComponent } from './components/requests/requests.component';
import { MyordersComponent } from './components/myorders/myorders.component';
import { MerchantordersComponent } from './components/merchantorders/merchantorders.component';
import { SinglepostComponent } from './components/singlepost/singlepost.component';
import { CommentComponent } from './components/comment/comment.component';
import { ListingComponent } from './components/listing/listing.component';
import { InteractionsComponent } from './components/interactions/interactions.component';
import { CreatepostComponent } from './components/createpost/createpost.component';
import { CreatelistingComponent } from './components/createlisting/createlisting.component';
import { OrderComponent } from './components/order/order.component';
import { AddMoneyComponent } from './components/add-money/add-money.component';
import { RolerequestComponent } from './components/rolerequest/rolerequest.component';
import { EditprofileComponent } from './components/editprofile/editprofile.component';
import { AuthInterceptor } from './auth.interceptor';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { MatButtonModule } from '@angular/material/button';
import { MatInputModule } from '@angular/material/input';
import { LayoutModule } from '@angular/cdk/layout';
import { MatToolbarModule } from '@angular/material/toolbar';
import { MatSidenavModule } from '@angular/material/sidenav';
import { MatIconModule } from '@angular/material/icon';
import { MatListModule } from '@angular/material/list';


@NgModule({
  declarations: [
    AppComponent,
    NavBarComponent,
    BaseComponent,
    FeedComponent,
    MarketplaceComponent,
    ProfileComponent,
    LoginComponent,
    SignUpComponent,
    RequestsComponent,
    MyordersComponent,
    MerchantordersComponent,
    SinglepostComponent,
    CommentComponent,
    ListingComponent,
    InteractionsComponent,
    CreatepostComponent,
    CreatelistingComponent,
    OrderComponent,
    AddMoneyComponent,
    RolerequestComponent,
    EditprofileComponent,

  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    FormsModule,
    ReactiveFormsModule,
    HttpClientModule,
    BrowserAnimationsModule,
    MatButtonModule,
    MatInputModule,
    LayoutModule,
    MatToolbarModule,
    MatSidenavModule,
    MatIconModule,
    MatListModule,
  ],
  providers: [
    {
      provide: HTTP_INTERCEPTORS,
      useClass: AuthInterceptor,
      multi: true,
    }
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
