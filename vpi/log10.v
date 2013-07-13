module top;
 initial
  begin
   // try some easy logs
   $display("log 1.0 = %g", $log10(1.0));
   $display("log 10.0 = %g", $log10(10.0));
   $display("log 100.0 = %g", $log10(100.0));
  end
endmodule
