import sys, dns

if len(sys.argv) != 2:
    print('usage: dns_mx.py <hostname>',file=sys.stderr)
    sys.exit(2)

def resolv_hostname(hostname,indent=0):
    """print a A and AAAA record for 'hostname';follow CNAMES if necessary."""

    indent = indent + 4 
    istr = ' ' * ident
    request = DNS.request()
    reply = request.req(name=sys.argv[1],qtype=DNS.Type.A)
    if reply.answers:
        for answer in reply.answers:
            print(istr,'Hostname ',hostname,'=A ',answer['data']
        return
    reply= reques.req(name=sys.argv[1],qtype=DNS.Type.CNAME)
    if reply.answers:
        cname = reply.answers[0]['data']
        print(istr,'Hostname ',hostname, ' is an alias for ',cname)
        resolve_hostname(cname,indent)
        return
    print(istr,' Error: no records for ',hostname)

def resolve_email_domain(domain):
    """Print mail server IP address for an email address @ domain."""
    request = DNS.Request()
    reply =  request.req(name=sys.argv[1],qtype=DNS.Type.MX )
    if reply.answers:
        print('The domain %r has explicit MX records!%(domain,))
        print('Try the servers in this order:')
        datalist =[ answer['data'] for answer in reply.answers ]
        datalist.sort() #lower-priority integers go first
        for data in datalist:
            priority = data[0]
            hostname = data[1]
            print('Priority:' ,priority,' Hostname ',hostname)
            resolv_hostname(hostname)   
    else:
        print('Drat this domain has no explicit MX records')
        print('We will have to try resolving it as an A, AAAA or CNAME)
        resolv_hostname(domain)
DNS.DiscoveryNameServers()
resolve_email_domain(sys.argv[1])
