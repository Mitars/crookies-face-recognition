import { TestBed } from '@angular/core/testing';

import { CrookieService } from './crookie.service';

describe('CrookieService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CrookieService = TestBed.get(CrookieService);
    expect(service).toBeTruthy();
  });
});
