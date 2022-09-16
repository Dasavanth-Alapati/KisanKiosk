import { ComponentFixture, TestBed } from '@angular/core/testing';

import { RolerequestComponent } from './rolerequest.component';

describe('RolerequestComponent', () => {
  let component: RolerequestComponent;
  let fixture: ComponentFixture<RolerequestComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ RolerequestComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(RolerequestComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
