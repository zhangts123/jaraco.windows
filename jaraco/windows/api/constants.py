# from error.h
NO_ERROR = 0
ERROR_INSUFFICIENT_BUFFER = 122
ERROR_BUFFER_OVERFLOW = 111
ERROR_NO_DATA = 232
ERROR_INVALID_PARAMETER = 87
ERROR_NOT_SUPPORTED = 50

# from WinNT.h
READ_CONTROL = 0x00020000
STANDARD_RIGHTS_REQUIRED = 0x000F0000
STANDARD_RIGHTS_READ = READ_CONTROL
STANDARD_RIGHTS_WRITE = READ_CONTROL
STANDARD_RIGHTS_EXECUTE = READ_CONTROL
STANDARD_RIGHTS_ALL = 0x001F0000

# from NTSecAPI.h
POLICY_VIEW_LOCAL_INFORMATION = 0x00000001
POLICY_VIEW_AUDIT_INFORMATION = 0x00000002
POLICY_GET_PRIVATE_INFORMATION = 0x00000004
POLICY_TRUST_ADMIN = 0x00000008
POLICY_CREATE_ACCOUNT = 0x00000010
POLICY_CREATE_SECRET = 0x00000020
POLICY_CREATE_PRIVILEGE = 0x00000040
POLICY_SET_DEFAULT_QUOTA_LIMITS = 0x00000080
POLICY_SET_AUDIT_REQUIREMENTS = 0x00000100
POLICY_AUDIT_LOG_ADMIN = 0x00000200
POLICY_SERVER_ADMIN = 0x00000400
POLICY_LOOKUP_NAMES = 0x00000800
POLICY_NOTIFICATION = 0x00001000

POLICY_ALL_ACCESS = (
	STANDARD_RIGHTS_REQUIRED |
	POLICY_VIEW_LOCAL_INFORMATION |
	POLICY_VIEW_AUDIT_INFORMATION |
	POLICY_GET_PRIVATE_INFORMATION |
	POLICY_TRUST_ADMIN |
	POLICY_CREATE_ACCOUNT |
	POLICY_CREATE_SECRET |
	POLICY_CREATE_PRIVILEGE |
	POLICY_SET_DEFAULT_QUOTA_LIMITS |
	POLICY_SET_AUDIT_REQUIREMENTS |
	POLICY_AUDIT_LOG_ADMIN |
	POLICY_SERVER_ADMIN |
	POLICY_LOOKUP_NAMES)


POLICY_READ = (
	STANDARD_RIGHTS_READ |
	POLICY_VIEW_AUDIT_INFORMATION |
	POLICY_GET_PRIVATE_INFORMATION)

POLICY_WRITE = (
	STANDARD_RIGHTS_WRITE |
	POLICY_TRUST_ADMIN |
	POLICY_CREATE_ACCOUNT |
	POLICY_CREATE_SECRET |
	POLICY_CREATE_PRIVILEGE |
	POLICY_SET_DEFAULT_QUOTA_LIMITS |
	POLICY_SET_AUDIT_REQUIREMENTS |
	POLICY_AUDIT_LOG_ADMIN |
	POLICY_SERVER_ADMIN)

POLICY_EXECUTE = (
	STANDARD_RIGHTS_EXECUTE |
	POLICY_VIEW_LOCAL_INFORMATION |
	POLICY_LOOKUP_NAMES)