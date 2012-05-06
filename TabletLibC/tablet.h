//
//  tablet.h
//  TabletLibC
//
//  Created by Anomalous Underdog on 5/6/12.
//
//  Copyright (c) 2012 Anomalous Underdog
//
//  Permission is hereby granted, free of charge, to any person obtaining a copy
//  of this software and associated documentation files (the "Software"), to
//  deal in the Software without restriction, including without limitation the
//  rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
//  sell copies of the Software, and to permit persons to whom the Software is
//  furnished to do so, subject to the following conditions:
//
//  The above copyright notice and this permission notice shall be included in
//  all copies or substantial portions of the Software.
//
//  THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
//  IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
//  FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
//  AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
//  LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
//  FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER
//  DEALINGS IN THE SOFTWARE.
//

#ifndef TabletLibC_tablet_h
#define TabletLibC_tablet_h

int init(void);
int stop(void);

long long get_point_x(void);
long long get_point_y(void);
long long get_point_z(void);
long long get_buttons(void);
double get_tilt_x(void);
double get_tilt_y(void);
double get_rotation(void);
double get_pressure(void);
double get_tangent_pressure(void);
long long get_vendor1(void);
long long get_vendor2(void);
long long get_vendor3(void);
long long get_vendor_id(void);
long long get_tablet_id(void);
long long get_pointer_id(void);
long long get_device_id(void);
long long get_system_tablet_id(void);
long long get_vendor_pointer_type(void);
long long get_vendor_pointer_serial_number(void);
long long get_vendor_unique_id(void);
long long get_capability_mask(void);
long long get_pointer_type(void);
long long get_enter_proximity(void);

#endif
