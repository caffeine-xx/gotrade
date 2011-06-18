
#line 1 "lexer.rl"
=begin

#line 18 "lexer.rl"

=end


#line 11 "lexer.c"
static const char _test_lexer_actions[] = {
	0, 1, 0, 1, 1, 1, 5, 1, 
	6, 1, 7, 2, 2, 3, 2, 2, 
	4
};

static const char _test_lexer_key_offsets[] = {
	0, 0, 2, 6, 8, 10
};

static const char _test_lexer_trans_keys[] = {
	48, 57, 43, 45, 48, 57, 48, 57, 
	48, 57, 48, 57, 0
};

static const char _test_lexer_single_lengths[] = {
	0, 0, 2, 0, 0, 0
};

static const char _test_lexer_range_lengths[] = {
	0, 1, 1, 1, 1, 1
};

static const char _test_lexer_index_offsets[] = {
	0, 0, 2, 6, 8, 10
};

static const char _test_lexer_trans_targs[] = {
	3, 0, 1, 1, 4, 0, 3, 2, 
	5, 2, 5, 2, 2, 2, 2, 0
};

static const char _test_lexer_trans_actions[] = {
	0, 0, 0, 0, 0, 0, 0, 7, 
	11, 5, 14, 9, 7, 5, 9, 0
};

static const char _test_lexer_to_state_actions[] = {
	0, 0, 1, 0, 0, 0
};

static const char _test_lexer_from_state_actions[] = {
	0, 0, 3, 0, 0, 0
};

static const char _test_lexer_eof_trans[] = {
	0, 0, 0, 13, 14, 15
};

static const int test_lexer_start = 2;
static const int test_lexer_first_final = 2;
static const int test_lexer_error = 0;

static const int test_lexer_en_main = 2;


#line 22 "lexer.rl"

def run_lexer(data)
  data = data.unpack("c*") if (data.is_a?(String))
  eof = data.length
  token_array = []

  
#line 76 "lexer.c"
	{
	cs = test_lexer_start;
	ts = 0;
	te = 0;
	act = 0;
	}

#line 29 "lexer.rl"
  
#line 86 "lexer.c"
	{
	int _klen;
	unsigned int _trans;
	const char *_acts;
	unsigned int _nacts;
	const char *_keys;

	if ( p == pe )
		goto _test_eof;
	if ( cs == 0 )
		goto _out;
_resume:
	_acts = _test_lexer_actions + _test_lexer_from_state_actions[cs];
	_nacts = (unsigned int) *_acts++;
	while ( _nacts-- > 0 ) {
		switch ( *_acts++ ) {
	case 1:
#line 1 "NONE"
	{ts = p;}
	break;
#line 107 "lexer.c"
		}
	}

	_keys = _test_lexer_trans_keys + _test_lexer_key_offsets[cs];
	_trans = _test_lexer_index_offsets[cs];

	_klen = _test_lexer_single_lengths[cs];
	if ( _klen > 0 ) {
		const char *_lower = _keys;
		const char *_mid;
		const char *_upper = _keys + _klen - 1;
		while (1) {
			if ( _upper < _lower )
				break;

			_mid = _lower + ((_upper-_lower) >> 1);
			if ( (*p) < *_mid )
				_upper = _mid - 1;
			else if ( (*p) > *_mid )
				_lower = _mid + 1;
			else {
				_trans += (_mid - _keys);
				goto _match;
			}
		}
		_keys += _klen;
		_trans += _klen;
	}

	_klen = _test_lexer_range_lengths[cs];
	if ( _klen > 0 ) {
		const char *_lower = _keys;
		const char *_mid;
		const char *_upper = _keys + (_klen<<1) - 2;
		while (1) {
			if ( _upper < _lower )
				break;

			_mid = _lower + (((_upper-_lower) >> 1) & ~1);
			if ( (*p) < _mid[0] )
				_upper = _mid - 2;
			else if ( (*p) > _mid[1] )
				_lower = _mid + 2;
			else {
				_trans += ((_mid - _keys)>>1);
				goto _match;
			}
		}
		_trans += _klen;
	}

_match:
_eof_trans:
	cs = _test_lexer_trans_targs[_trans];

	if ( _test_lexer_trans_actions[_trans] == 0 )
		goto _again;

	_acts = _test_lexer_actions + _test_lexer_trans_actions[_trans];
	_nacts = (unsigned int) *_acts++;
	while ( _nacts-- > 0 )
	{
		switch ( *_acts++ )
		{
	case 2:
#line 1 "NONE"
	{te = p+1;}
	break;
	case 3:
#line 8 "lexer.rl"
	{act = 1;}
	break;
	case 4:
#line 11 "lexer.rl"
	{act = 2;}
	break;
	case 5:
#line 11 "lexer.rl"
	{te = p;p--;{
      emit(:POSINT, data, token_array, ts, te)
    }}
	break;
	case 6:
#line 14 "lexer.rl"
	{te = p;p--;{
      emit(:integer_literal, data, token_array, ts, te)
    }}
	break;
	case 7:
#line 1 "NONE"
	{	switch( act ) {
	case 1:
	{{p = ((te))-1;}
      emit(:DAYOFMONTH, data, token_array, ts, te)
    }
	break;
	case 2:
	{{p = ((te))-1;}
      emit(:POSINT, data, token_array, ts, te)
    }
	break;
	}
	}
	break;
#line 212 "lexer.c"
		}
	}

_again:
	_acts = _test_lexer_actions + _test_lexer_to_state_actions[cs];
	_nacts = (unsigned int) *_acts++;
	while ( _nacts-- > 0 ) {
		switch ( *_acts++ ) {
	case 0:
#line 1 "NONE"
	{ts = 0;}
	break;
#line 225 "lexer.c"
		}
	}

	if ( cs == 0 )
		goto _out;
	if ( ++p != pe )
		goto _resume;
	_test_eof: {}
	if ( p == eof )
	{
	if ( _test_lexer_eof_trans[cs] > 0 ) {
		_trans = _test_lexer_eof_trans[cs] - 1;
		goto _eof_trans;
	}
	}

	_out: {}
	}

#line 30 "lexer.rl"

  puts token_array.inspect
end


def emit(token_name, data, target_array, ts, te)
  target_array << {
    :name => token_name.to_sym, 
    :value => data[ts..te].pack("c*") ,
    :extra => [token_name.to_sym, target_array, ts, te]
  }
end

print run_lexer("11")
