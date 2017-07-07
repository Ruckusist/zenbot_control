var c = module.exports = {}

// mongo configuration
c.mongo = {}
c.mongo.host = process.env.MONGODB_PORT_27017_TCP_ADDR || 'localhost'
c.mongo.port = 27017
c.mongo.db = 'zenbot4'
c.mongo.username = null
c.mongo.password = null
c.mongo.replicaSet = null

// default selector. only used if omitting [selector] argument from a command.
c.selector = 'poloniex.ZEC-BTC'
// name of default trade strategy
c.strategy = 'trend_ema'

// Exchange API keys:
// to enable Poloniex trading, enter your API credentials:
c.poloniex = {}
c.poloniex.key = 'YOUR-API-KEY'
c.poloniex.secret = 'YOUR-SECRET'
// please note: poloniex does not support market orders via the API
// Optional stop-order triggers:
// sell if price drops below this % of bought price (0 to disable)
c.sell_stop_pct = 0
// buy if price surges above this % of sold price (0 to disable)
c.buy_stop_pct = 0
// enable trailing sell stop when reaching this % profit (0 to disable)
c.profit_stop_enable_pct = 0
// maintain a trailing stop this % below the high-water mark of profit
c.profit_stop_pct = 2

// Order execution rules:

// avoid trading at a slippage above this pct
c.max_slippage_pct = 5
// buy with this % of currency balance (WARNING : sim won't work properly if you set this value to 100)
c.buy_pct = 99
// sell with this % of asset balance (WARNING : sim won't work properly if you set this value to 100)
c.sell_pct = 99
// ms to adjust non-filled order after
c.order_adjust_time = 5000
// avoid selling at a loss below this pct
c.max_sell_loss_pct = 10
// ms to poll order status
c.order_poll_time = 5000
// ms to wait for settlement (after an order cancel)
c.wait_for_settlement = 5000
// % to mark up or down price for orders
c.markup_pct = 2
// become a market taker (high fees) or a market maker (low fees)
c.order_type = 'maker'

// Misc options:

// default # days for backfill and sim commands
c.days = 14
// ms to poll new trades at
c.poll_trades = 15000
// amount of currency to start simulations with
c.currency_capital = 0
// amount of asset to start simulations with
c.asset_capital = 0.1
// for sim, reverse time at the end of the graph, normalizing buy/hold to 0
c.symmetrical = false
// number of periods to calculate RSI at
c.rsi_periods = 14
// period to record balances for stats
c.balance_snapshot_period = '15m'
// avg. amount of slippage to apply to sim trades
c.avg_slippage_pct = 0.145
