package fix44;
type AdvSide struct {
	enum AdvSideEnum {
		BUY
		SELL
		CROSS
		TRADE
	}
	Value AdvSideEnum
}
