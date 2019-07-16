import { TestBed } from '@angular/core/testing';

import { CrookiesService } from './crookies.service';

describe('CrookiesService', () => {
  beforeEach(() => TestBed.configureTestingModule({}));

  it('should be created', () => {
    const service: CrookiesService = TestBed.get(CrookiesService);
    expect(service).toBeTruthy();
  });
});
