#include <stdio.h>
#include <math.h>

#include "veriuser.h"
//#include "cv_veriuser.h"
#include "vpi_user.h"
//#include "cv_vpi_user.h"

/* prototypes */
static int my_log10(void);
extern void register_my_systfs(void);

static int my_log10(void)
{
 double d1, d2;
 vpiHandle systfref, argsiter, argh;
 struct t_vpi_value wrkval;

 /* get system function that invoked C routine */
 systfref = vpi_handle(vpiSysTfCall, NULL);
 /* get iterator (list) of passed arguments */
 argsiter = vpi_iterate(vpiArgument, systfref);
 /* get the one argument - add loop for more args */
 argh = vpi_scan(argsiter);

 /* get the argument value */
 wrkval.format = vpiRealVal;
 vpi_get_value(argh, &wrkval);
 d1 =  wrkval.value.real;

 /* any C library function can go here */
 d2 = log10(d1);

 /* return value by assigning to calling systf handle */
 wrkval.value.real = d2;
 vpi_put_value(systfref, &wrkval, NULL, vpiNoDelay);
 return(0);
}

/* my boiler plate for registering system tasks */
void (*vlog_startup_routines[]) () =
{
 register_my_systfs,
 0
};

/*
 * register my user system tasks and functions
 */
void register_my_systfs(void)
{
 p_vpi_systf_data systf_data_p;

 static s_vpi_systf_data systf_data_list[] = {
  { vpiSysFunc, vpiSysFuncReal, "$log10", my_log10, NULL, NULL, NULL },
  { 0, 0, NULL, NULL, NULL, NULL, NULL }
 };

 systf_data_p = &(systf_data_list[0]);
 while (systf_data_p->type != 0) vpi_register_systf(systf_data_p++);
}
