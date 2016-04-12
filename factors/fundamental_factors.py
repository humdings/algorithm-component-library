import numpy as np

from quantopian.pipeline.factors import CustomFactor

from quantopian.pipeline.data.builtin import USEquityPricing

from quantopian.pipeline.data import morningstar


class EBIT_EV(CustomFactor):

    window_length = 1
    inputs = [morningstar.income_statement.ebit,
              morningstar.valuation.enterprise_value]

    def compute(self, today, assets, out, ebit, ev):
        out[:] = ebit[-1] / ev[-1]


class CashFlowToPrice(CustomFactor):

    inputs = [USEquityPricing.close,
              morningstar.cash_flow_statement.free_cash_flow]

    window_length = 30

    def compute(self, today, assets, out, close_price, cash_flow):
        cfp = np.log(cash_flow / close_price)
        out[:] = np.nanmean(cfp, axis=0)
