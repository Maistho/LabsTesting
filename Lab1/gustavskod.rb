class FuncNode < Node
   def initialize(name, block, idlist)
      @name = name
      @block = block
      @idlist = idlist
   end

   def eval(argslist)
      evArgslist = argslist.map {|arg|
         begin
            arg.eval()
         rescue NoMethodError
         arg
         end}
      IdNode.increaseScope
      if evArgslist.size() ==  @idlist.size()
         @idlist.each_with_index {|id, i|
            begin
               id.setVar(evArgslist[i].eval())
            rescue NoMethodError
               id.setVar(evArgslist[i])
         end}
      else
         puts "\nFel antal argument till funktion: " + @name
         exit()
      end
      ret = @block.eval()
      if ret.is_a?(ReturnNode)
         ret = ret.getValue
         IdNode.decreaseScope
         return ret
      elsif ret.is_a?(AbortNode)
         puts "\nOtillaaten anvaendning av 'avbryt' i funktion: " + @name
         puts "Anvaend 'skicka tillbaka' foer att avbryta funktioner."
         exit()
      end
      IdNode.decreaseScope
      return ret
   end
end