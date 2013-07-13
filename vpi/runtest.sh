#/usr/bin

iverilog-vpi hello.c
iverilog -ohello.vvp hello.v
vvp -M. -mhello hello.vvp

iverilog-vpi log10.c
iverilog -olog10.vvp log10.v
vvp -M. -mlog10 log10.vvp

iverilog-vpi vpi_add.c
iverilog -ovpi_add.vvp vpi_add.v
vvp -M. -mvpi_add vpi_add.vvp
