module top;
initial
  begin
    $display("%d=%d+%d", $vpi_add(2,1), 2, 1);
  end
endmodule
