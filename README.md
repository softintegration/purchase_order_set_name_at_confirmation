Purchase order reference attribution at confirmation
----------------------------------------------------
This module make attribution of the reference at the confirmation of the Purchase order.
>__Note__:Modules that override the create method of __purchase.order__ and installed with this module,must take in account
> the context variable __set_purchase_order_name__,this variable must be __True__ in order to generate the sequence at the creation or the behaviour of the sequence generation will be unexpected.  



