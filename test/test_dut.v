
`timescale 1ns/10ps

/*--------------------------
*  test add over float
* -------------------------*/
module test_over_float();

parameter C_WIDTH = 8;

 reg  [C_WIDTH-1:0] reg_a;
 reg  [C_WIDTH-1:0] reg_b;
 wire [C_WIDTH-1:0] reg_c;
 reg  [C_WIDTH-1:0] exp_c;

 initial begin
  #0 reg_a = 8'hFF; reg_b = 8'hFF;
  exp_c = $vpi_add(reg_a, reg_b);

  if (reg_c != exp_c)
    $display("ERROR HW add %d = %d + %d, SW add %d = %d + %d", reg_c, reg_a, reg_b, exp_c, reg_a, reg_b);
//  $finsih;
 end

 Add #(.C_WIDTH(C_WIDTH))
 u_add ( .a(reg_a), .b(reg_b), .c(reg_c));

endmodule


/*------------------------------
*  test normal add
* -----------------------------*/
module test_normal();

parameter C_WIDTH = 8;

 reg  [C_WIDTH-1:0] reg_a;
 reg  [C_WIDTH-1:0] reg_b;
 wire [C_WIDTH-1:0] reg_c;
 reg  [C_WIDTH-1:0] exp_c;

 initial begin
  #0 reg_a = 8'h00; reg_b = 8'h01;
  exp_c = $vpi_add(reg_a, reg_b);

  if (reg_c != $vpi_add(reg_a, reg_b))
    $display("ERROR HW add %d = %d + %d, SW add %d = %d + %d", reg_c, reg_a, reg_b, exp_c, reg_a, reg_b);
//  $finsih;
 end

 Add #(.C_WIDTH(C_WIDTH))
 u_add ( .a(reg_a), .b(reg_b), .c(reg_c));

endmodule


