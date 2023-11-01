class RecordStatus:
    ACTIVE = 0
    DELETED = 1
    INACTIVE = 2

    CHOICES = (
        (ACTIVE, 'Active'),
        (DELETED, 'Deleted'),
        (INACTIVE, 'In Active'),
    )


class Department:
    SALES = 0
    ADMIN = 1
    SUPPORT = 2
    IT = 3
    ENGINEER = 4
    HR = 5
    MANAGEMENT = 6

    CHOICES = (
        (SALES, 'Sales'),
        (ADMIN, 'Admin'),
        (SUPPORT, 'Support'),
        (IT, 'IT'),
        (ENGINEER, 'Engineer'),
        (HR, 'HR'),
        (MANAGEMENT, 'Management'),
    )


class Position:
    INTERN = 0
    EXECUTIVE = 1
    SR_EXECUTIVE = 2
    TEAM_LEAD = 3
    MANAGER = 4
    CTO = 5
    CFO = 6
    CEO = 7

    CHOICES = (
        (INTERN, 'Intern'),
        (EXECUTIVE, 'Executive'),
        (SR_EXECUTIVE, 'Sr Executive'),
        (TEAM_LEAD, 'Team Lead'),
        (MANAGER, 'Manager'),
        (CTO, 'CTO'),
        (CFO, 'CFO'),
        (CEO, 'CEO'),
    )


class Gender:
    MALE = 0
    FEMALE = 1
    OTHER = 2

    CHOICES = (
        (MALE, 'Male'),
        (FEMALE, 'Female'),
        (OTHER, 'Other'),
    )


class ClientType:
    CUSTOMER = 0
    VENDOR = 1

    CHOICES = (
        (CUSTOMER, 'Customer'),
        (VENDOR, 'Vendor'),
    )


class OrderType:
    OUTWARD = 0
    INWARD = 1

    CHOICES = (
        (OUTWARD, 'Outward'),
        (INWARD, 'Inward'),
    )


class OrderStatus:
    NEW = 0
    ACCEPTED = 1
    INPROCESS = 2
    READY = 3
    DISPATCHED = 4
    DELIVERED = 5
    CANCELLED = 6

    CHOICES = (
        (NEW, 'New'),
        (ACCEPTED, 'Accepted'),
        (INPROCESS, 'In Process'),
        (READY, 'Ready'),
        (DISPATCHED, 'Dispatched'),
        (DELIVERED, 'Delivered'),
        (CANCELLED, 'Cancelled'),
    )


class PaymentType:
    ADVANCE = 0
    INSTALLMENT = 0

    CHOICES = (
        (ADVANCE, 'Advance'),
        (INSTALLMENT, 'Installment'),
    )


class PaymentMode:
    CASH = 0
    UPI = 1
    CARD = 2
    CHEQUE = 3
    DRAFT = 4
    NEFT = 5
    IMPS = 6

    CHOICES = (
        (CASH, 'Cash'),
        (UPI, 'UPI'),
        (CARD, 'Card'),
        (CHEQUE, 'Cheque'),
        (DRAFT, 'Draft'),
        (NEFT, 'NEFT'),
        (IMPS, 'IMPS'),
    )