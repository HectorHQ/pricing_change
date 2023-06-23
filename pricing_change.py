import pandas as pd
import requests
import json
import streamlit as st
from openpyxl import load_workbook


st.set_page_config("Bundled Orders Fee Change",page_icon=':memo:',layout="wide",initial_sidebar_state='expanded')
st.title(':blue[Bundle] Orders Fee Change :memo:')




bearer_token = str(st.text_input("Insert Bearer Token"))

st.cache()
headers = {
    "authority": "api.getnabis.com",
    "accept": "*/*",
    "accept-language": "es-ES,es;q=0.9", #"en-GB,en-US;q=0.9,en;q=0.8"
    "authorization": bearer_token,
    # Already added when you pass json=
    # 'content-type': 'application/json',
    "origin": "https://app.getnabis.com",
    "referer": "https://app.getnabis.com/",
    "sec-fetch-dest": "empty",
    "sec-fetch-mode": "cors",
    "sec-fetch-site": "same-site",
    "sec-gpc": "1",
    "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.134 Safari/537.36",
}

st.cache()
def all_admin_orders_accounting_page(order_number):
    json_data = {
        "operationName": "AllAdminOrdersAccountingPage",
        "variables": {
            "pageInfo": {
                "numItemsPerPage": 25,
                "orderBy": [
                    {
                        "attribute": "date",
                        "order": "DESC",
                    },
                    {
                        "attribute": "createdAt",
                        "order": "DESC",
                    },
                ],
                "page": 1,
            },
            "search": order_number,
            "status": [
                "DELIVERED",
                "DELIVERED_WITH_EDITS",
                "DELAYED",
                "REJECTED",
                "ATTEMPTED",
            ],
        },
        "query": "query AllAdminOrdersAccountingPage($organizationId: ID, $search: String, $status: [OrderStatusEnum], $paymentStatus: [OrderPaymentStatusEnum], $disputeStatus: [OrderDisputeStatus!], $start: DateTime, $end: DateTime, $paymentProcessedAtStart: DateTime, $paymentProcessedAtEnd: DateTime, $paymentSentAtStart: DateTime, $paymentSentAtEnd: DateTime, $paidAtStart: DateTime, $paidAtEnd: DateTime, $irn: String, $orderFees: [String], $pageInfo: PageInfoInput, $collectionStatus: [BrandFeesCollectionCollectionStatusEnum]) {\n  viewer {\n    allAdminAccountingOrders(organizationId: $organizationId, search: $search, status: $status, irn: $irn, paymentStatus: $paymentStatus, disputeStatus: $disputeStatus, start: $start, end: $end, paymentProcessedAtStart: $paymentProcessedAtStart, paymentProcessedAtEnd: $paymentProcessedAtEnd, paymentSentAtStart: $paymentSentAtStart, paymentSentAtEnd: $paymentSentAtEnd, paidAtStart: $paidAtStart, paidAtEnd: $paidAtEnd, orderFees: $orderFees, pageInfo: $pageInfo, collectionStatus: $collectionStatus) {\n      results {\n        id\n        adminNotes\n        action\n        accountingNotes\n        ACHAmountCollectedRetailer\n        ACHAmountPaidBrand\n        internalNotes\n        createdAt\n        creditMemo\n        date\n        daysTillPaymentDue\n        distroFees\n        dueToBrand\n        discount\n        surcharge\n        edited\n        exciseTax\n        exciseTaxCollected\n        extraFees\n        gmv\n        gmvCollected\n        wholesaleGmv\n        priceDifference\n        irn\n        manifestGDriveFileId\n        apSummaryGDriveFileId\n        apSummaryS3FileLink\n        invoicesS3FileLink\n        packingListS3FileLink\n        mustPayPreviousBalance\n        nabisDiscount\n        name\n        notes\n        number\n        isSampleDemo\n        parentOrder {\n          id\n          totalGMV\n          shouldRemoveMinFee\n          __typename\n        }\n        paymentStatus\n        paymentTermsRequestStatus\n        hasSingleQBInvoice\n        hasMultiQBInvoices\n        hasMultiAQBInvoice\n        hasMultiBQBInvoice\n        hasMultiCQBInvoice\n        hasMultiC1QBInvoice\n        hasMultiC2QBInvoice\n        isAfterQuickbooksDeploy\n        lastPaymentTermOrderChange {\n          submitter {\n            id\n            firstName\n            lastName\n            isAdmin\n            __typename\n          }\n          id\n          description\n          createdAt\n          __typename\n        }\n        orderFees {\n          ...feeOrderFragment\n          __typename\n        }\n        pricingFee\n        pricingPercentage\n        basePricing {\n          pricingFee\n          pricingPercentage\n          __typename\n        }\n        status\n        creator {\n          id\n          email\n          firstName\n          lastName\n          __typename\n        }\n        licensedLocation {\n          ...licensedLocationFragment\n          __typename\n        }\n        organization {\n          id\n          doingBusinessAs\n          alias\n          name\n          owner {\n            id\n            email\n            firstName\n            lastName\n            __typename\n          }\n          __typename\n        }\n        site {\n          id\n          name\n          address1\n          address2\n          city\n          state\n          zip\n          pocName\n          pocPhoneNumber\n          pocEmail\n          licensedLocationId\n          licensedLocation {\n            id\n            __typename\n          }\n          __typename\n        }\n        paidAt\n        paymentMethod\n        remittedAt\n        factorStatus\n        calculateMoneyValues {\n          subtotal\n          orderDiscount\n          lineItemDiscounts\n          totalExciseTax\n          totalBalance\n          discountedSubtotal\n          taxRate\n          netOffTotal\n          __typename\n        }\n        nabisManifestNotes\n        referrer\n        orderFiles {\n          ...orderFileFragment\n          __typename\n        }\n        writeOffReasons\n        paymentSentAt\n        processingAt\n        ...lastAccountingOrderIssues\n        brandFeesCollection {\n          ...BrandFeesCollectionFragment\n          user {\n            id\n            firstName\n            lastName\n            email\n            __typename\n          }\n          __typename\n        }\n        willAutoRegenerateInvoices\n        __typename\n      }\n      pageInfo {\n        page\n        numItemsPerPage\n        orderBy {\n          attribute\n          order\n          __typename\n        }\n        totalNumItems\n        totalNumPages\n        __typename\n      }\n      nextOrders {\n        number\n        date\n        id\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment feeOrderFragment on OrderFee {\n  id\n  feeId\n  feeName\n  feePrice\n  feeNotes\n  createdBy {\n    firstName\n    lastName\n    email\n    __typename\n  }\n  fee {\n    ...feeFragment\n    __typename\n  }\n  __typename\n}\n\nfragment feeFragment on Fee {\n  id\n  basePrice\n  description\n  name\n  feeType\n  groupTag\n  startDate\n  endDate\n  isArchived\n  __typename\n}\n\nfragment licensedLocationFragment on LicensedLocation {\n  id\n  name\n  address1\n  address2\n  city\n  state\n  zip\n  siteCategory\n  lat\n  lng\n  billingAddress1\n  billingAddress2\n  billingAddressCity\n  billingAddressState\n  billingAddressZip\n  warehouseId\n  isArchived\n  doingBusinessAs\n  noExciseTax\n  phoneNumber\n  printCoas\n  hoursBusiness\n  hoursDelivery\n  deliveryByApptOnly\n  specialProtocol\n  schedulingSoftwareRequired\n  schedulingSoftwareLink\n  centralizedPurchasingNotes\n  payByCheck\n  collectionNotes\n  deliveryNotes\n  collect1PocFirstName\n  collect1PocLastName\n  collect1PocTitle\n  collect1PocNumber\n  collect1PocEmail\n  collect1PocAllowsText\n  collect1PreferredContactMethod\n  collect2PocFirstName\n  collect2PocLastName\n  collect2PocTitle\n  collect2PocNumber\n  collect2PocEmail\n  collect2PocAllowsText\n  collect2PreferredContactMethod\n  delivery1PocFirstName\n  delivery1PocLastName\n  delivery1PocTitle\n  delivery1PocNumber\n  delivery1PocEmail\n  delivery1PocAllowsText\n  delivery1PreferredContactMethod\n  delivery2PocFirstName\n  delivery2PocLastName\n  delivery2PocTitle\n  delivery2PocNumber\n  delivery2PocEmail\n  delivery2PocAllowsText\n  delivery2PreferredContactMethod\n  unmaskedId\n  qualitativeRating\n  creditRating\n  trustLevelNabis\n  trustLevelInEffect\n  isOnNabisTracker\n  locationNotes\n  infoplus\n  w9Link\n  taxIdentificationNumber\n  sellerPermitLink\n  nabisMaxTerms\n  __typename\n}\n\nfragment orderFileFragment on OrderFile {\n  id\n  type\n  s3Link\n  mimeType\n  notes\n  createdAt\n  updatedAt\n  orderId\n  __typename\n}\n\nfragment lastAccountingOrderIssues on AccountingOrder {\n  lastDispute {\n    id\n    reason\n    initiatedNotes\n    initiatedAt\n    issueType\n    resolvedAt\n    __typename\n  }\n  lastNonpayment {\n    id\n    reason\n    initiatedNotes\n    initiatedAt\n    issueType\n    __typename\n  }\n  __typename\n}\n\nfragment BrandFeesCollectionFragment on BrandFeesCollection {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  submitterId\n  collectionStatus\n  collectionStatusUpdatedAt\n  notes\n  __typename\n}\n",
    }

    response = requests.post(
        "https://api.getnabis.com/graphql/admin", headers=headers, json=json_data
    )
    return response.json()

st.cache()
def pricing_change(qb_invoice_data,pricing_amt):
    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data["orderId"],
                'pricingFee': pricing_amt,
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHACRetailerUnconfirmed\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  mustPayExternalBalance\n  externalPaymentMin\n  externalPaymentDesired\n  externalPaymentNotes\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  isCreditMemoLocked\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    return response.json()

st.cache()
def regenerate_inv_B(qb_invoice_data):
    json_data = {
    'operationName': 'GenerateQuickbooksInvoice',
    'variables': {
        'input': {
            "orderId": qb_invoice_data["orderId"],
            "pricingPercentage": qb_invoice_data["pricingPercentage"],
            "pricingFee": qb_invoice_data["pricingFee"],
            "nabisDiscount": qb_invoice_data["nabisDiscount"],
            'invoiceTypesToGenerate': [
                'B',
            ],
        },
    },
    'query': 'mutation GenerateQuickbooksInvoice($input: GenerateQuickbooksInvoiceInput!) {\n  generateQuickbooksInvoice(input: $input) {\n    orderId\n    __typename\n  }\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    return response.json()

st.cache()
def generate_qb_single_invoice(qb_invoice_data):

    json_data = {
        "operationName": "GenerateQuickbooksInvoice",
        "variables": {
            "input": {
                "orderId": qb_invoice_data["orderId"],
                "pricingPercentage": qb_invoice_data["pricingPercentage"],
                "pricingFee": qb_invoice_data["pricingFee"],
                "nabisDiscount": qb_invoice_data["nabisDiscount"],
                "invoiceTypesToGenerate": [
                    "SINGLE",
                ],
            },
        },
        "query": "mutation GenerateQuickbooksInvoice($input: GenerateQuickbooksInvoiceInput!) {\n  generateQuickbooksInvoice(input: $input) {\n    orderId\n    __typename\n  }\n}\n",
    }

    response = requests.post(
        "https://api.getnabis.com/graphql/admin", headers=headers, json=json_data
    )
    return response.json()

st.cache()
def percentage_fee_change(qb_invoice_data,pct_fee):
    json_data = {
        'operationName': 'UpdateOrder',
        'variables': {
            'input': {
                'id': qb_invoice_data["orderId"],
                'pricingPercentage': pct_fee,
            },
            'isFromOrderForm': False,
        },
        'query': 'mutation UpdateOrder($input: UpdateOrderInput!, $isFromOrderForm: Boolean) {\n  updateOrder(input: $input, isFromOrderForm: $isFromOrderForm) {\n    changedOrder {\n      ...orderFragment\n      shipments {\n        ...shipmentFragment\n        __typename\n      }\n      __typename\n    }\n    __typename\n  }\n}\n\nfragment orderFragment on Order {\n  action\n  accountingNotes\n  additionalDiscount\n  adminNotes\n  createdAt\n  date\n  daysTillPaymentDue\n  paymentDueDate\n  totalAmountDue\n  requestedDaysTillPaymentDue\n  discount\n  distroFees\n  estimatedArrivalTimeAfter\n  estimatedArrivalTimeBefore\n  exciseTax\n  exciseTaxCollected\n  extraFees\n  gmv\n  gmvCollected\n  id\n  infoplus\n  internalNotes\n  irn\n  isArchived\n  manifestGDriveFileId\n  invoicesS3FileLink\n  name\n  notes\n  number\n  orgLicenseNum\n  paymentStatus\n  promotionsDiscount\n  siteLicenseNum\n  status\n  timeWindow\n  warehouseId\n  surcharge\n  mustPayPreviousBalance\n  nabisDiscount\n  issueReason\n  pricingFee\n  pricingPercentage\n  retailerConfirmationStatus\n  retailerNotes\n  creditMemo\n  netGmv\n  secondaryInfoplus\n  orderInventoryStatus\n  asnInventoryStatus\n  isEditableByBrand\n  isAtStartingStatus\n  shouldEnableOrderForm\n  isReceived\n  metrcWarehouseId\n  referrer\n  isSampleDemo\n  paymentTermsRequestStatus\n  brandManifestNotes\n  nabisManifestNotes\n  retailerManifestNotes\n  qrcodeS3FileLink\n  metrcManifestS3FileLink\n  isPrinted\n  isStaged\n  isCrossHubRetailTransfer\n  driverConfirmedAt\n  isSingleHubOrigin\n  firstShipmentId\n  lastShipmentId\n  lastNonReturnShipmentId\n  pickupDropoffWarehouseId\n  manufacturerOrgId\n  ACHAmountCollectedRetailer\n  ACHACRetailerUnconfirmed\n  ACHAmountPaidBrand\n  isExciseTaxable\n  orderLockdown {\n    ...orderLockdownFragment\n    __typename\n  }\n  mustPayExternalBalance\n  externalPaymentMin\n  externalPaymentDesired\n  externalPaymentNotes\n  __typename\n}\n\nfragment orderLockdownFragment on OrderLockdown {\n  id\n  createdAt\n  updatedAt\n  deletedAt\n  isArchived\n  orderEditLockdownTimestamp\n  isCreditMemoLocked\n  __typename\n}\n\nfragment shipmentFragment on Shipment {\n  id\n  orderId\n  originLicensedLocationId\n  destinationLicensedLocationId\n  status\n  stagingAreaId\n  isUnloaded\n  unloaderId\n  isLoaded\n  loaderId\n  arrivalTime\n  departureTime\n  isShipped\n  vehicleId\n  driverId\n  previousShipmentId\n  nextShipmentId\n  infoplusOrderId\n  infoplusAsnId\n  infoplusOrderInventoryStatus\n  infoplusAsnInventoryStatus\n  createdAt\n  updatedAt\n  shipmentNumber\n  queueOrder\n  isStaged\n  isPrinted\n  arrivalTimeAfter\n  arrivalTimeBefore\n  fulfillability\n  pickers\n  shipmentType\n  intaken\n  outtaken\n  metrcWarehouseLicenseNumber\n  __typename\n}\n',
    }

    response = requests.post('https://api.getnabis.com/graphql/admin', headers=headers, json=json_data)
    return response.json()


st.cache()
def main(list_orders):
    
    for order in list_orders:

        order_number = order
        order_data = all_admin_orders_accounting_page(order_number)

        flat_fee_amt = flat_fee_amt_dict[order_number]
        trigger = pct_fee_minimum[order_number] 

        qb_invoice_data = {
            "orderId": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['id'],
            "pricingPercentage": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['pricingPercentage'],
            "pricingFee": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['pricingFee'],
            "nabisDiscount": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['nabisDiscount'],
        }

        pricing_change(qb_invoice_data,flat_fee_amt)
        if trigger == False:
            pct_fee = 0.001
            percentage_fee_change(qb_invoice_data,pct_fee)
        st.code(f'{order} Processed')
    
st.cache()       
def main_regenerate(list_orders):
    
    for order in list_orders:
        order_number = order
        order_data = all_admin_orders_accounting_page(order_number)

        Letter = letter_dict[order_number]

        qb_invoice_data = {
            "orderId": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['id'],
            "pricingPercentage": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['pricingPercentage'],
            "pricingFee": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['pricingFee'],
            "nabisDiscount": order_data['data']['viewer']['allAdminAccountingOrders']['results'][0]['nabisDiscount'],
        }

        if Letter == "b":
            regenerate_inv_B(qb_invoice_data)
        else:    
            generate_qb_single_invoice(qb_invoice_data)

        st.code(f'{order}' + ' Regenerated')

st.cache()
def load_excel(file_path):
    book = load_workbook(file_path, data_only=True)
    writer = pd.ExcelWriter("temp.xlsx", engine="openpyxl")
    writer.book = book
    writer.save()
    writer.close()
    df = pd.read_excel("temp.xlsx")
    return df

col1,col2 = st.columns([2,1])
with col1:
    list_orders = st.file_uploader('Upload List of invoices file.',accept_multiple_files=False)
    flat_fee_amt = 0

if list_orders is not None:
        df = load_excel(list_orders)
        df['Invoice'] = df['Order'].astype('str')
        df['Flat Fee Allocation'] = df['Flat Fee Allocation'].astype('float').round(2)
        flat_fee_amt_dict = dict(zip(df['Invoice'],df['Flat Fee Allocation']))
        pct_fee_minimum = dict(zip(df['Invoice'],df['Trigger']))
        letter_dict = dict(zip(df['Invoice'],df['Letter']))
        count_invoices = df.shape
        st.write(f'{count_invoices[0]} Invoices to Update')
        
        with col2:
            selection = st.radio('Update Flat Fee or Regenerate Invoice',options=['Update Fee','Regenerate Invoices'])
            if selection == 'Update Fee':
                    st.caption('Click Button below to process')
                    submit_to_update = st.button('Update Flat Fee')
                    if submit_to_update:
                        st.cache_data()
                        main(df["Invoice"])

            elif selection == 'Regenerate Invoices':            
                    st.caption('Click Button below to process')
                    submit_to_regenerate_single = st.button('Regenerate Invoice')
                    if submit_to_regenerate_single:
                        st.cache_data()
                        main_regenerate(df["Invoice"])



st.markdown('---')
left_col,center_col,right_col = st.columns(3)

with center_col:
    st.title('**Powered by HQ**')
    st.image('https://www.dropbox.com/s/twrl9exjs8piv7t/Headquarters%20transparent%20light%20logo.png?dl=1')

