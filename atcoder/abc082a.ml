let f a b = int_of_float (ceil ((a +. b) /. 2.0));;
Scanf.scanf "%f %f" f
|> Printf.printf "%d\n"
