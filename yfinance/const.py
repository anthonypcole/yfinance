_BASE_URL_ = 'https://query2.finance.yahoo.com'
_ROOT_URL_ = 'https://finance.yahoo.com'

fundamentals_keys = {
    'financials': ["TaxEffectOfUnusualItems", "TaxRateForCalcs", "NormalizedEBITDA", "NormalizedDilutedEPS",
                   "NormalizedBasicEPS", "TotalUnusualItems", "TotalUnusualItemsExcludingGoodwill",
                   "NetIncomeFromContinuingOperationNetMinorityInterest", "ReconciledDepreciation",
                   "ReconciledCostOfRevenue", "EBITDA", "EBIT", "NetInterestIncome", "InterestExpense",
                   "InterestIncome", "ContinuingAndDiscontinuedDilutedEPS", "ContinuingAndDiscontinuedBasicEPS",
                   "NormalizedIncome", "NetIncomeFromContinuingAndDiscontinuedOperation", "TotalExpenses",
                   "RentExpenseSupplemental", "ReportedNormalizedDilutedEPS", "ReportedNormalizedBasicEPS",
                   "TotalOperatingIncomeAsReported", "DividendPerShare", "DilutedAverageShares", "BasicAverageShares",
                   "DilutedEPS", "DilutedEPSOtherGainsLosses", "TaxLossCarryforwardDilutedEPS",
                   "DilutedAccountingChange", "DilutedExtraordinary", "DilutedDiscontinuousOperations",
                   "DilutedContinuousOperations", "BasicEPS", "BasicEPSOtherGainsLosses", "TaxLossCarryforwardBasicEPS",
                   "BasicAccountingChange", "BasicExtraordinary", "BasicDiscontinuousOperations",
                   "BasicContinuousOperations", "DilutedNIAvailtoComStockholders", "AverageDilutionEarnings",
                   "NetIncomeCommonStockholders", "OtherunderPreferredStockDividend", "PreferredStockDividends",
                   "NetIncome", "MinorityInterests", "NetIncomeIncludingNoncontrollingInterests",
                   "NetIncomeFromTaxLossCarryforward", "NetIncomeExtraordinary", "NetIncomeDiscontinuousOperations",
                   "NetIncomeContinuousOperations", "EarningsFromEquityInterestNetOfTax", "TaxProvision",
                   "PretaxIncome", "OtherIncomeExpense", "OtherNonOperatingIncomeExpenses", "SpecialIncomeCharges",
                   "GainOnSaleOfPPE", "GainOnSaleOfBusiness", "OtherSpecialCharges", "WriteOff",
                   "ImpairmentOfCapitalAssets", "RestructuringAndMergernAcquisition", "SecuritiesAmortization",
                   "EarningsFromEquityInterest", "GainOnSaleOfSecurity", "NetNonOperatingInterestIncomeExpense",
                   "TotalOtherFinanceCost", "InterestExpenseNonOperating", "InterestIncomeNonOperating",
                   "OperatingIncome", "OperatingExpense", "OtherOperatingExpenses", "OtherTaxes",
                   "ProvisionForDoubtfulAccounts", "DepreciationAmortizationDepletionIncomeStatement",
                   "DepletionIncomeStatement", "DepreciationAndAmortizationInIncomeStatement", "Amortization",
                   "AmortizationOfIntangiblesIncomeStatement", "DepreciationIncomeStatement", "ResearchAndDevelopment",
                   "SellingGeneralAndAdministration", "SellingAndMarketingExpense", "GeneralAndAdministrativeExpense",
                   "OtherGandA", "InsuranceAndClaims", "RentAndLandingFees", "SalariesAndWages", "GrossProfit",
                   "CostOfRevenue", "TotalRevenue", "ExciseTaxes", "OperatingRevenue", "LossAdjustmentExpense",
                   "NetPolicyholderBenefitsAndClaims", "PolicyholderBenefitsGross", "PolicyholderBenefitsCeded",
                   "OccupancyAndEquipment", "ProfessionalExpenseAndContractServicesExpense", "OtherNonInterestExpense",
                    "CreditCard",                             # New
                    "CreditLossesProvision",                  # New
                    "CostOfGoodsAndServices",                 # New
                    "DividendIncome",                         # New
                    "FinancingRevenue",                       # New
                    "ForeignExchangeTradingGains",            # New
                    "GainonSaleofInvestmentProperty",         # New
                    "GainonSaleofLoans",                      # New
                    "IncomeLossfromContOps",                  # New
                    "IncomeLossInclMI",                       # New
                    "InterestExpenseForDeposit",              # New
                    "InterestExpenseForFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResell", # New
                    "InterestExpenseForLongTermDebtAndCapitalSecurities",  # New
                    "InterestExpenseForShortTermDebt",        # New
                    "InterestIncomeAfterProvisionForLoanLoss",# New
                    "InterestIncomeFromDeposits",             # New
                    "InterestIncomeFromFederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResell", # New
                    "InterestIncomeFromLeases",               # New
                    "InterestIncomeFromLoans",                # New
                    "InvestmentBankingProfit",                # New
                    "LossonExtinguishmentofDebt",             # New
                    "NetIncomeAvailtoCommon",                 # New
                    "NetOccupancyExpense",                    # New
                    "OtherCustomerServices",                  # New
                    "OtherInterestExpense",                   # New
                    "OtherInterestIncome",                    # New
                    "PaymentsForLoans",                       # New
                    "ProceedsFromLoans",                      # New
                    "SecuritiesActivities",                   # New
                    "ServiceChargeOnDepositorAccounts",       # New
                    "TotalMoneyMarketInvestments",            # New
                    "TradingGainLoss",                        # New
                    "TrustFeesbyCommissions"                  # New
                   ],
    'balance-sheet': ["TreasurySharesNumber", "PreferredSharesNumber", "OrdinarySharesNumber", "ShareIssued", "NetDebt",
                      "TotalDebt", "TangibleBookValue", "InvestedCapital", "WorkingCapital", "NetTangibleAssets",
                      "CapitalLeaseObligations", "CommonStockEquity", "PreferredStockEquity", "TotalCapitalization",
                      "TotalEquityGrossMinorityInterest", "MinorityInterest", "StockholdersEquity",
                      "OtherEquityInterest", "GainsLossesNotAffectingRetainedEarnings", "OtherEquityAdjustments",
                      "FixedAssetsRevaluationReserve", "ForeignCurrencyTranslationAdjustments",
                      "MinimumPensionLiabilities", "UnrealizedGainLoss", "TreasuryStock", "RetainedEarnings",
                      "AdditionalPaidInCapital", "CapitalStock", "OtherCapitalStock", "CommonStock", "PreferredStock",
                      "TotalPartnershipCapital", "GeneralPartnershipCapital", "LimitedPartnershipCapital",
                      "TotalLiabilitiesNetMinorityInterest", "TotalNonCurrentLiabilitiesNetMinorityInterest",
                      "OtherNonCurrentLiabilities", "LiabilitiesHeldforSaleNonCurrent", "RestrictedCommonStock",
                      "PreferredSecuritiesOutsideStockEquity", "DerivativeProductLiabilities", "EmployeeBenefits",
                      "NonCurrentPensionAndOtherPostretirementBenefitPlans", "NonCurrentAccruedExpenses",
                      "DuetoRelatedPartiesNonCurrent", "TradeandOtherPayablesNonCurrent",
                      "NonCurrentDeferredLiabilities", "NonCurrentDeferredRevenue",
                      "NonCurrentDeferredTaxesLiabilities", "LongTermDebtAndCapitalLeaseObligation",
                      "LongTermCapitalLeaseObligation", "LongTermDebt", "LongTermProvisions", "CurrentLiabilities",
                      "OtherCurrentLiabilities", "CurrentDeferredLiabilities", "CurrentDeferredRevenue",
                      "CurrentDeferredTaxesLiabilities", "CurrentDebtAndCapitalLeaseObligation",
                      "CurrentCapitalLeaseObligation", "CurrentDebt", "OtherCurrentBorrowings", "LineOfCredit",
                      "CommercialPaper", "CurrentNotesPayable", "PensionandOtherPostRetirementBenefitPlansCurrent",
                      "CurrentProvisions", "PayablesAndAccruedExpenses", "CurrentAccruedExpenses", "InterestPayable",
                      "Payables", "OtherPayable", "DuetoRelatedPartiesCurrent", "DividendsPayable", "TotalTaxPayable",
                      "IncomeTaxPayable", "AccountsPayable", "TotalAssets", "TotalNonCurrentAssets",
                      "OtherNonCurrentAssets", "DefinedPensionBenefit", "NonCurrentPrepaidAssets",
                      "NonCurrentDeferredAssets", "NonCurrentDeferredTaxesAssets", "DuefromRelatedPartiesNonCurrent",
                      "NonCurrentNoteReceivables", "NonCurrentAccountsReceivable", "FinancialAssets",
                      "InvestmentsAndAdvances", "OtherInvestments", "InvestmentinFinancialAssets",
                      "HeldToMaturitySecurities", "AvailableForSaleSecurities",
                      "FinancialAssetsDesignatedasFairValueThroughProfitorLossTotal", "TradingSecurities",
                      "LongTermEquityInvestment", "InvestmentsinJointVenturesatCost",
                      "InvestmentsInOtherVenturesUnderEquityMethod", "InvestmentsinAssociatesatCost",
                      "InvestmentsinSubsidiariesatCost", "InvestmentProperties", "GoodwillAndOtherIntangibleAssets",
                      "OtherIntangibleAssets", "Goodwill", "NetPPE", "AccumulatedDepreciation", "GrossPPE", "Leases",
                      "ConstructionInProgress", "OtherProperties", "MachineryFurnitureEquipment",
                      "BuildingsAndImprovements", "LandAndImprovements", "Properties", "CurrentAssets",
                      "OtherCurrentAssets", "HedgingAssetsCurrent", "AssetsHeldForSaleCurrent", "CurrentDeferredAssets",
                      "CurrentDeferredTaxesAssets", "RestrictedCash", "PrepaidAssets", "Inventory",
                      "InventoriesAdjustmentsAllowances", "OtherInventories", "FinishedGoods", "WorkInProcess",
                      "RawMaterials", "Receivables", "ReceivablesAdjustmentsAllowances", "OtherReceivables",
                      "DuefromRelatedPartiesCurrent", "TaxesReceivable", "AccruedInterestReceivable", "NotesReceivable",
                      "LoansReceivable", "AccountsReceivable", "AllowanceForDoubtfulAccountsReceivable",
                      "GrossAccountsReceivable", "CashCashEquivalentsAndShortTermInvestments",
                      "OtherShortTermInvestments", "CashAndCashEquivalents", "CashEquivalents", "CashFinancial",
                      "CashCashEquivalentsAndFederalFundsSold",
                        "AdvanceFromFederalHomeLoanBanks",            # Added by JB 2024--9-5
                        "BankOwnedLifeInsurance",                      
                        "CashAndDueFromBanks",                      
                        "CommercialLoan",                              
                        "ConsumerLoan",                               
                        "CustomerAcceptances",                        
                        "CustomerAccounts",                           
                        "DepositsbyBank",                             
                        "FederalFundsPurchased",                       
                        "FederalFundsPurchasedAndSecuritiesSoldUnderAgreementToRepurchase",  
                        "FederalFundsSold",                           
                        "FederalFundsSoldAndSecuritiesPurchaseUnderAgreementsToResell",     
                        "FederalHomeLoanBankStock",                    
                        "ForeclosedAssets",                            
                        "GrossLoan",                                   
                        "GrossNotesReceivable",                       
                        "InterestBearingDepositsAssets",              
                        "InterestBearingDepositsLiabilities",         
                        "LoansHeldForSale",                          
                        "MoneyMarketInvestments",                     
                        "MortgageLoan",                               
                        "NetLoan",                                    
                        "NonInterestBearingDeposits",                 
                        "PolicyholderFunds",                           
                        "PolicyLoans",                              
                        "SecuritySoldNotYetRepurchased",             
                        "SeparateAccountAssets",                       
                        "SeparateAccountBusiness",                    
                        "UnpaidLossAndLossReserve",                   
                        "UnearnedIncome",                            
                        "UnearnedPremiums"                           
                      ],
    'cash-flow': ["ForeignSales", "DomesticSales", "AdjustedGeographySegmentData", "FreeCashFlow",
                  "RepurchaseOfCapitalStock", "RepaymentOfDebt", "IssuanceOfDebt", "IssuanceOfCapitalStock",
                  "CapitalExpenditure", "InterestPaidSupplementalData", "IncomeTaxPaidSupplementalData",
                  "EndCashPosition", "OtherCashAdjustmentOutsideChangeinCash", "BeginningCashPosition",
                  "EffectOfExchangeRateChanges", "ChangesInCash", "OtherCashAdjustmentInsideChangeinCash",
                  "CashFlowFromDiscontinuedOperation", "FinancingCashFlow", "CashFromDiscontinuedFinancingActivities",
                  "CashFlowFromContinuingFinancingActivities", "NetOtherFinancingCharges", "InterestPaidCFF",
                  "ProceedsFromStockOptionExercised", "CashDividendsPaid", "PreferredStockDividendPaid",
                  "CommonStockDividendPaid", "NetPreferredStockIssuance", "PreferredStockPayments",
                  "PreferredStockIssuance", "NetCommonStockIssuance", "CommonStockPayments", "CommonStockIssuance",
                  "NetIssuancePaymentsOfDebt", "NetShortTermDebtIssuance", "ShortTermDebtPayments",
                  "ShortTermDebtIssuance", "NetLongTermDebtIssuance", "LongTermDebtPayments", "LongTermDebtIssuance",
                  "InvestingCashFlow", "CashFromDiscontinuedInvestingActivities",
                  "CashFlowFromContinuingInvestingActivities", "NetOtherInvestingChanges", "InterestReceivedCFI",
                  "DividendsReceivedCFI", "NetInvestmentPurchaseAndSale", "SaleOfInvestment", "PurchaseOfInvestment",
                  "NetInvestmentPropertiesPurchaseAndSale", "SaleOfInvestmentProperties",
                  "PurchaseOfInvestmentProperties", "NetBusinessPurchaseAndSale", "SaleOfBusiness",
                  "PurchaseOfBusiness", "NetIntangiblesPurchaseAndSale", "SaleOfIntangibles", "PurchaseOfIntangibles",
                  "NetPPEPurchaseAndSale", "SaleOfPPE", "PurchaseOfPPE", "CapitalExpenditureReported",
                  "OperatingCashFlow", "CashFromDiscontinuedOperatingActivities",
                  "CashFlowFromContinuingOperatingActivities", "TaxesRefundPaid", "InterestReceivedCFO",
                  "InterestPaidCFO", "DividendReceivedCFO", "DividendPaidCFO", "ChangeInWorkingCapital",
                  "ChangeInOtherWorkingCapital", "ChangeInOtherCurrentLiabilities", "ChangeInOtherCurrentAssets",
                  "ChangeInPayablesAndAccruedExpense", "ChangeInAccruedExpense", "ChangeInInterestPayable",
                  "ChangeInPayable", "ChangeInDividendPayable", "ChangeInAccountPayable", "ChangeInTaxPayable",
                  "ChangeInIncomeTaxPayable", "ChangeInPrepaidAssets", "ChangeInInventory", "ChangeInReceivables",
                  "ChangesInAccountReceivables", "OtherNonCashItems", "ExcessTaxBenefitFromStockBasedCompensation",
                  "StockBasedCompensation", "UnrealizedGainLossOnInvestmentSecurities", "ProvisionandWriteOffofAssets",
                  "AssetImpairmentCharge", "AmortizationOfSecurities", "DeferredTax", "DeferredIncomeTax",
                  "DepreciationAmortizationDepletion", "Depletion", "DepreciationAndAmortization",
                  "AmortizationCashFlow", "AmortizationOfIntangibles", "Depreciation", "OperatingGainsLosses",
                  "PensionAndEmployeeBenefitExpense", "EarningsLossesFromEquityInvestments",
                  "GainLossOnInvestmentSecurities", "NetForeignCurrencyExchangeGainLoss", "GainLossOnSaleOfPPE",
                  "GainLossOnSaleOfBusiness", "NetIncomeFromContinuingOperations",
                  "CashFlowsfromusedinOperatingActivitiesDirect", "TaxesRefundPaidDirect", "InterestReceivedDirect",
                  "InterestPaidDirect", "DividendsReceivedDirect", "DividendsPaidDirect", "ClassesofCashPayments",
                  "OtherCashPaymentsfromOperatingActivities", "PaymentsonBehalfofEmployees",
                  "PaymentstoSuppliersforGoodsandServices", "ClassesofCashReceiptsfromOperatingActivities",
                  "OtherCashReceiptsfromOperatingActivities", "ReceiptsfromGovernmentGrants", "ReceiptsfromCustomers",
                  "ChangeInFederalFundsAndSecuritiesSoldForRepurchase",  # newly added JB 2024-9-5 
                  "NetProceedsPaymentForLoan",                           # newly added JB 2024-9-5             
                  "ProvisionForLoanLeaseAndOtherLosses"                  # newly added JB 2024-9-5                
                  ]}

_PRICE_COLNAMES_ = ['Open', 'High', 'Low', 'Close', 'Adj Close']

quote_summary_valid_modules = (
    "summaryProfile",  # contains general information about the company
    "summaryDetail",  # prices + volume + market cap + etc
    "assetProfile",  # summaryProfile + company officers
    "fundProfile",
    "price",  # current prices
    "quoteType",  # quoteType
    "esgScores",  # Environmental, social, and governance (ESG) scores, sustainability and ethical performance of companies
    "incomeStatementHistory",
    "incomeStatementHistoryQuarterly",
    "balanceSheetHistory",
    "balanceSheetHistoryQuarterly",
    "cashFlowStatementHistory",
    "cashFlowStatementHistoryQuarterly",
    "defaultKeyStatistics",  # KPIs (PE, enterprise value, EPS, EBITA, and more)
    "financialData",  # Financial KPIs (revenue, gross margins, operating cash flow, free cash flow, and more)
    "calendarEvents",  # future earnings date
    "secFilings",  # SEC filings, such as 10K and 10Q reports
    "upgradeDowngradeHistory",  # upgrades and downgrades that analysts have given a company's stock
    "institutionOwnership",  # institutional ownership, holders and shares outstanding
    "fundOwnership",  # mutual fund ownership, holders and shares outstanding
    "majorDirectHolders",
    "majorHoldersBreakdown",
    "insiderTransactions",  # insider transactions, such as the number of shares bought and sold by company executives
    "insiderHolders",  # insider holders, such as the number of shares held by company executives
    "netSharePurchaseActivity",  # net share purchase activity, such as the number of shares bought and sold by company executives
    "earnings",  # earnings history
    "earningsHistory",
    "earningsTrend",  # earnings trend
    "industryTrend",
    "indexTrend",
    "sectorTrend",
    "recommendationTrend",
    "futuresChain",
)
