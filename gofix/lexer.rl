=begin
%%{
  machine test_lexer;
  action print_state {
    print [ "fcurs ",fcurs," fc ",fc, " ts ", ts, " te ", te, "\n"]
  }
  action print_stuff {
    print data[ts..te].pack("c*")
  }
  integer=('+'|'-')?[0-9]+ %print_state;
  value=[a-z]+ %print_state;
  field= (
      integer
      '=' 
      value
      '|'? );
  main := |*
    field => {
      emit(:field_literal, data, token_array, ts, te)
    };
  *|;
}%%
=end

%% write data;

def run_lexer(data)
  data = data.unpack("c*") if (data.is_a?(String))
  eof = data.length
  token_array = []

  %% write init;
  %% write exec;

  puts token_array.inspect
end


def emit(token_name, data, target_array, ts, te)
  target_array << {
    :name => token_name.to_sym, 
    :value => data[ts..te].pack("c*") ,
    :extra => [token_name.to_sym, target_array, ts, te]
  }
  return target_array
end

print run_lexer("12=abc|")
