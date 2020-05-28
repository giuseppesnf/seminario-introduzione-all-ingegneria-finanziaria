from QuantLib import *
import matplotlib.pyplot as plot
import numpy as np

today = Date(27, September, 2019)
Settings.instance().evaluationDate = today
option = EuropeanOption(PlainVanillaPayoff(Option.Call, 106404.15), EuropeanExercise(Date(27, September, 2024)))
put = EuropeanOption(PlainVanillaPayoff(Option.Put, 106404.15), EuropeanExercise(Date(27, September, 2024)))

u = SimpleQuote(259594.0)
r = SimpleQuote(0.0169)
sigma = SimpleQuote(0.2)

riskFreeCurve = FlatForward(0, TARGET(), QuoteHandle(r), Actual360())
volatility = BlackConstantVol(0, TARGET(), QuoteHandle(sigma), Actual360())

process = BlackScholesProcess(QuoteHandle(u), YieldTermStructureHandle(riskFreeCurve), BlackVolTermStructureHandle(volatility))

engine = AnalyticEuropeanEngine(process)

call.setPricingEngine(engine)

print(call.NPV())
print(call.delta())
print(call.gamma())
print(call.vega())

put.setPricingEngine(engine)

print(put.NPV())
print(put.delta())
print(put.gamma())
print(put.vega())

c = (call.NPV())
p = (put.NPV())


f, ax = plot.subplots()
xs = np.linspace(100.00, 40000.00)
ys = []




for x in xs:for x in xs:
    u.setValue(x)
    ys.append(call.NPV())

ax.set_title("Option Value")
_ = ax.plot(xs, ys)
plot.show()



f, ax = plot.subplots()
xs = np.linspace(100.00, 40000.00)
ys = []




for x in xs:
    u.setValue(x)
    ys.append(put.NPV())

ax.set_title("Option Value")
_ = ax.plot(xs, ys)
plot.show()

model = HestonModel(
    HestonProcess(YieldTermStructureHandle(riskFreeCurve),
                  YieldTermStructureHandle(FlatForward(0, TARGET(), 0.0, Actual360())),
                  QuoteHandle(u),
                  0.004, 0.1, 0.01, 0.05, -0.75))
engine = AnalyticHestonEngine(model)
option.setPricingEngine(engine)
print(option.NPV())

engine = MCEuropeanEngine(process, "PseudoRandom",
                          timeSteps=20,
                          requiredSamples=250000)
option.setPricingEngine(engine)
print(option.NPV())

# ...

c = (call.NPV())
p = (option.NPV())
A0 = 193984
PVK = 38129

# modello put call parity
