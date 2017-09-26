from mininet.topo import Topo

class NreDemo( Topo ):
    "Demonstration topology for the Scinet NRE demo"

    def __init__( self ):
        Topo.__init__( self )

        s1 = self.addSwitch( 's1' )
        s2 = self.addSwitch( 's2' )
        s3 = self.addSwitch( 's3' )
        s4 = self.addSwitch( 's4' )
        s5 = self.addSwitch( 's5' )

        perf1 = self.addHost( 'perf1' )
        perf2 = self.addHost( 'perf2' )
        perf3 = self.addHost( 'perf3' )
        perf4 = self.addHost( 'perf4' )
        perf5 = self.addHost( 'perf5' )

        h1 = self.addHost( 'h1' )
        h2 = self.addHost( 'h2' )

        self.addLink(s1, s2)
        self.addLink(s2, s3)
        self.addLink(s3, s4)
        self.addLink(s4, s5)
        self.addLink(s2, s4)

        self.addLink(perf1, s1)
        self.addLink(perf2, s2)
        self.addLink(perf3, s3)
        self.addLink(perf4, s4)
        self.addLink(perf5, s5)

        self.addLink(h1, s1)
        self.addLink(h2, s5)

topos = { 'nredemo': ( lambda:NreDemo() ) }
