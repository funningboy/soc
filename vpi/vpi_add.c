
#include <stdio.h>
#include <math.h>

#include "veriuser.h"
//#include "cv_veriuser.h"
#include "vpi_user.h"
//#include "cv_vpi_user.h"


// Implements the vpi_add system task
static int vpi_add(char *userdata) {
  vpiHandle systfref, args_iter, argh;
  struct t_vpi_value argval_a, argval_b;
  unsigned char value_a, value_b;

  // Obtain a handle to the argument list
  systfref = vpi_handle(vpiSysTfCall, NULL);
  args_iter = vpi_iterate(vpiArgument, systfref);

  // Grab the value of the first argument
  argh = vpi_scan(args_iter);
  argval_a.format = vpiIntVal;
  vpi_get_value(argh, &argval_a);
  value_a = argval_a.value.integer;
  vpi_printf("VPI routine received a %d\n", value_a);

  // Grab the value of the sec argument
  argh = vpi_scan(args_iter);
  argval_b.format = vpiIntVal;
  vpi_get_value(argh, &argval_b);
  value_b = argval_b.value.integer;
  vpi_printf("VPI routine received b %d\n", value_b);

  // vpi_add the value and put it back as first argument
  argval_a.value.integer = value_a + value_b;
  vpi_printf("VPI add %d=%d+%d\n", argval_a.value.integer, value_a, value_b);

  // return pp
  vpi_put_value(systfref, &argval_a, NULL, vpiNoDelay);

  // Cleanup and return
  vpi_free_object(args_iter);
  return 0;
}

// Registers the vpi_add system task
void register_vpi_add() {
 p_vpi_systf_data systf_data_p;

 static s_vpi_systf_data systf_data_list[] = {
  { vpiSysFunc, vpiSysFuncReal, "$vpi_add", vpi_add, NULL, NULL, NULL },
  { 0, 0, NULL, NULL, NULL, NULL, NULL }
 };

 systf_data_p = &(systf_data_list[0]);
 while (systf_data_p->type != 0) vpi_register_systf(systf_data_p++);
}

// Contains a zero-terminated list of functions that have to be called at startup
void (*vlog_startup_routines[])() = {
  register_vpi_add,
  0
};
