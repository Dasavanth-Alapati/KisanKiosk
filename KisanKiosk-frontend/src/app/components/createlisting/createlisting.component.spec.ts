import { ComponentFixture, TestBed } from '@angular/core/testing';

import { CreatelistingComponent } from './createlisting.component';

describe('CreatelistingComponent', () => {
  let component: CreatelistingComponent;
  let fixture: ComponentFixture<CreatelistingComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      declarations: [ CreatelistingComponent ]
    })
    .compileComponents();

    fixture = TestBed.createComponent(CreatelistingComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
