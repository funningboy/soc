
module Add #(parameter C_WIDTH = 32) (a, b, c);
  input [C_WIDTH-1:0] a;
  input [C_WIDTH-1:0] b;
  output[C_WIDTH-1:0] c;
  assign c = a + b;
endmodule
