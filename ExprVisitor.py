# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete generic visitor for a parse tree produced by ExprParser.

class ExprVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by ExprParser#file_.
    def visitFile_(self, ctx:ExprParser.File_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#interactive.
    def visitInteractive(self, ctx:ExprParser.InteractiveContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#eval_.
    def visitEval_(self, ctx:ExprParser.Eval_Context):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#func_type.
    def visitFunc_type(self, ctx:ExprParser.Func_typeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statements.
    def visitStatements(self, ctx:ExprParser.StatementsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement.
    def visitStatement(self, ctx:ExprParser.StatementContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#single_compound_stmt.
    def visitSingle_compound_stmt(self, ctx:ExprParser.Single_compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#statement_newline.
    def visitStatement_newline(self, ctx:ExprParser.Statement_newlineContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#simple_stmts.
    def visitSimple_stmts(self, ctx:ExprParser.Simple_stmtsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#simple_stmt.
    def visitSimple_stmt(self, ctx:ExprParser.Simple_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#compound_stmt.
    def visitCompound_stmt(self, ctx:ExprParser.Compound_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignment.
    def visitAssignment(self, ctx:ExprParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotated_rhs.
    def visitAnnotated_rhs(self, ctx:ExprParser.Annotated_rhsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#augassign.
    def visitAugassign(self, ctx:ExprParser.AugassignContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#return_stmt.
    def visitReturn_stmt(self, ctx:ExprParser.Return_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#raise_stmt.
    def visitRaise_stmt(self, ctx:ExprParser.Raise_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#pass_stmt.
    def visitPass_stmt(self, ctx:ExprParser.Pass_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#break_stmt.
    def visitBreak_stmt(self, ctx:ExprParser.Break_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#continue_stmt.
    def visitContinue_stmt(self, ctx:ExprParser.Continue_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#global_stmt.
    def visitGlobal_stmt(self, ctx:ExprParser.Global_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#nonlocal_stmt.
    def visitNonlocal_stmt(self, ctx:ExprParser.Nonlocal_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#del_stmt.
    def visitDel_stmt(self, ctx:ExprParser.Del_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#yield_stmt.
    def visitYield_stmt(self, ctx:ExprParser.Yield_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assert_stmt.
    def visitAssert_stmt(self, ctx:ExprParser.Assert_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#import_stmt.
    def visitImport_stmt(self, ctx:ExprParser.Import_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#import_name.
    def visitImport_name(self, ctx:ExprParser.Import_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#import_from.
    def visitImport_from(self, ctx:ExprParser.Import_fromContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#import_from_targets.
    def visitImport_from_targets(self, ctx:ExprParser.Import_from_targetsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#import_from_as_names.
    def visitImport_from_as_names(self, ctx:ExprParser.Import_from_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#import_from_as_name.
    def visitImport_from_as_name(self, ctx:ExprParser.Import_from_as_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#dotted_as_names.
    def visitDotted_as_names(self, ctx:ExprParser.Dotted_as_namesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#dotted_as_name.
    def visitDotted_as_name(self, ctx:ExprParser.Dotted_as_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#dotted_name.
    def visitDotted_name(self, ctx:ExprParser.Dotted_nameContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#block.
    def visitBlock(self, ctx:ExprParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#decorators.
    def visitDecorators(self, ctx:ExprParser.DecoratorsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#class_def.
    def visitClass_def(self, ctx:ExprParser.Class_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#class_def_raw.
    def visitClass_def_raw(self, ctx:ExprParser.Class_def_rawContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#function_def.
    def visitFunction_def(self, ctx:ExprParser.Function_defContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#function_def_raw.
    def visitFunction_def_raw(self, ctx:ExprParser.Function_def_rawContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#params.
    def visitParams(self, ctx:ExprParser.ParamsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#parameters.
    def visitParameters(self, ctx:ExprParser.ParametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#slash_no_default.
    def visitSlash_no_default(self, ctx:ExprParser.Slash_no_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#slash_with_default.
    def visitSlash_with_default(self, ctx:ExprParser.Slash_with_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_etc.
    def visitStar_etc(self, ctx:ExprParser.Star_etcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#kwds.
    def visitKwds(self, ctx:ExprParser.KwdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#param_no_default.
    def visitParam_no_default(self, ctx:ExprParser.Param_no_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#param_no_default_star_annotation.
    def visitParam_no_default_star_annotation(self, ctx:ExprParser.Param_no_default_star_annotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#param_with_default.
    def visitParam_with_default(self, ctx:ExprParser.Param_with_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#param_maybe_default.
    def visitParam_maybe_default(self, ctx:ExprParser.Param_maybe_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#param.
    def visitParam(self, ctx:ExprParser.ParamContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#param_star_annotation.
    def visitParam_star_annotation(self, ctx:ExprParser.Param_star_annotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#annotation.
    def visitAnnotation(self, ctx:ExprParser.AnnotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_annotation.
    def visitStar_annotation(self, ctx:ExprParser.Star_annotationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#default.
    def visitDefault(self, ctx:ExprParser.DefaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#if_stmt.
    def visitIf_stmt(self, ctx:ExprParser.If_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#elif_stmt.
    def visitElif_stmt(self, ctx:ExprParser.Elif_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#else_block.
    def visitElse_block(self, ctx:ExprParser.Else_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#while_stmt.
    def visitWhile_stmt(self, ctx:ExprParser.While_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#for_stmt.
    def visitFor_stmt(self, ctx:ExprParser.For_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#with_stmt.
    def visitWith_stmt(self, ctx:ExprParser.With_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#with_item.
    def visitWith_item(self, ctx:ExprParser.With_itemContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#try_stmt.
    def visitTry_stmt(self, ctx:ExprParser.Try_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#except_block.
    def visitExcept_block(self, ctx:ExprParser.Except_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#except_star_block.
    def visitExcept_star_block(self, ctx:ExprParser.Except_star_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#finally_block.
    def visitFinally_block(self, ctx:ExprParser.Finally_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#match_stmt.
    def visitMatch_stmt(self, ctx:ExprParser.Match_stmtContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#subject_expr.
    def visitSubject_expr(self, ctx:ExprParser.Subject_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#case_block.
    def visitCase_block(self, ctx:ExprParser.Case_blockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#guard.
    def visitGuard(self, ctx:ExprParser.GuardContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#patterns.
    def visitPatterns(self, ctx:ExprParser.PatternsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#pattern.
    def visitPattern(self, ctx:ExprParser.PatternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#as_pattern.
    def visitAs_pattern(self, ctx:ExprParser.As_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#or_pattern.
    def visitOr_pattern(self, ctx:ExprParser.Or_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#closed_pattern.
    def visitClosed_pattern(self, ctx:ExprParser.Closed_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#literal_pattern.
    def visitLiteral_pattern(self, ctx:ExprParser.Literal_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#literal_expr.
    def visitLiteral_expr(self, ctx:ExprParser.Literal_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#complex_number.
    def visitComplex_number(self, ctx:ExprParser.Complex_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#signed_number.
    def visitSigned_number(self, ctx:ExprParser.Signed_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#signed_real_number.
    def visitSigned_real_number(self, ctx:ExprParser.Signed_real_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#real_number.
    def visitReal_number(self, ctx:ExprParser.Real_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#imaginary_number.
    def visitImaginary_number(self, ctx:ExprParser.Imaginary_numberContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#capture_pattern.
    def visitCapture_pattern(self, ctx:ExprParser.Capture_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#pattern_capture_target.
    def visitPattern_capture_target(self, ctx:ExprParser.Pattern_capture_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#wildcard_pattern.
    def visitWildcard_pattern(self, ctx:ExprParser.Wildcard_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#value_pattern.
    def visitValue_pattern(self, ctx:ExprParser.Value_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#attr.
    def visitAttr(self, ctx:ExprParser.AttrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#name_or_attr.
    def visitName_or_attr(self, ctx:ExprParser.Name_or_attrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#group_pattern.
    def visitGroup_pattern(self, ctx:ExprParser.Group_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sequence_pattern.
    def visitSequence_pattern(self, ctx:ExprParser.Sequence_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#open_sequence_pattern.
    def visitOpen_sequence_pattern(self, ctx:ExprParser.Open_sequence_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#maybe_sequence_pattern.
    def visitMaybe_sequence_pattern(self, ctx:ExprParser.Maybe_sequence_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#maybe_star_pattern.
    def visitMaybe_star_pattern(self, ctx:ExprParser.Maybe_star_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_pattern.
    def visitStar_pattern(self, ctx:ExprParser.Star_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#mapping_pattern.
    def visitMapping_pattern(self, ctx:ExprParser.Mapping_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#items_pattern.
    def visitItems_pattern(self, ctx:ExprParser.Items_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#key_value_pattern.
    def visitKey_value_pattern(self, ctx:ExprParser.Key_value_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#double_star_pattern.
    def visitDouble_star_pattern(self, ctx:ExprParser.Double_star_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#class_pattern.
    def visitClass_pattern(self, ctx:ExprParser.Class_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#positional_patterns.
    def visitPositional_patterns(self, ctx:ExprParser.Positional_patternsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#keyword_patterns.
    def visitKeyword_patterns(self, ctx:ExprParser.Keyword_patternsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#keyword_pattern.
    def visitKeyword_pattern(self, ctx:ExprParser.Keyword_patternContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type_alias.
    def visitType_alias(self, ctx:ExprParser.Type_aliasContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type_params.
    def visitType_params(self, ctx:ExprParser.Type_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type_param_seq.
    def visitType_param_seq(self, ctx:ExprParser.Type_param_seqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type_param.
    def visitType_param(self, ctx:ExprParser.Type_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type_param_bound.
    def visitType_param_bound(self, ctx:ExprParser.Type_param_boundContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type_param_default.
    def visitType_param_default(self, ctx:ExprParser.Type_param_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type_param_starred_default.
    def visitType_param_starred_default(self, ctx:ExprParser.Type_param_starred_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expressions.
    def visitExpressions(self, ctx:ExprParser.ExpressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#expression.
    def visitExpression(self, ctx:ExprParser.ExpressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#yield_expr.
    def visitYield_expr(self, ctx:ExprParser.Yield_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_expressions.
    def visitStar_expressions(self, ctx:ExprParser.Star_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_expression.
    def visitStar_expression(self, ctx:ExprParser.Star_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_named_expressions.
    def visitStar_named_expressions(self, ctx:ExprParser.Star_named_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_named_expression.
    def visitStar_named_expression(self, ctx:ExprParser.Star_named_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#assignment_expression.
    def visitAssignment_expression(self, ctx:ExprParser.Assignment_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#named_expression.
    def visitNamed_expression(self, ctx:ExprParser.Named_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#disjunction.
    def visitDisjunction(self, ctx:ExprParser.DisjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#conjunction.
    def visitConjunction(self, ctx:ExprParser.ConjunctionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#inversion.
    def visitInversion(self, ctx:ExprParser.InversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#comparison.
    def visitComparison(self, ctx:ExprParser.ComparisonContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#compare_op_bitwise_or_pair.
    def visitCompare_op_bitwise_or_pair(self, ctx:ExprParser.Compare_op_bitwise_or_pairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#eq_bitwise_or.
    def visitEq_bitwise_or(self, ctx:ExprParser.Eq_bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#noteq_bitwise_or.
    def visitNoteq_bitwise_or(self, ctx:ExprParser.Noteq_bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lte_bitwise_or.
    def visitLte_bitwise_or(self, ctx:ExprParser.Lte_bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lt_bitwise_or.
    def visitLt_bitwise_or(self, ctx:ExprParser.Lt_bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#gte_bitwise_or.
    def visitGte_bitwise_or(self, ctx:ExprParser.Gte_bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#gt_bitwise_or.
    def visitGt_bitwise_or(self, ctx:ExprParser.Gt_bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#notin_bitwise_or.
    def visitNotin_bitwise_or(self, ctx:ExprParser.Notin_bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#in_bitwise_or.
    def visitIn_bitwise_or(self, ctx:ExprParser.In_bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#isnot_bitwise_or.
    def visitIsnot_bitwise_or(self, ctx:ExprParser.Isnot_bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#is_bitwise_or.
    def visitIs_bitwise_or(self, ctx:ExprParser.Is_bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitwise_or.
    def visitBitwise_or(self, ctx:ExprParser.Bitwise_orContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitwise_xor.
    def visitBitwise_xor(self, ctx:ExprParser.Bitwise_xorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#bitwise_and.
    def visitBitwise_and(self, ctx:ExprParser.Bitwise_andContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#shift_expr.
    def visitShift_expr(self, ctx:ExprParser.Shift_exprContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#sum.
    def visitSum(self, ctx:ExprParser.SumContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#term.
    def visitTerm(self, ctx:ExprParser.TermContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#factor.
    def visitFactor(self, ctx:ExprParser.FactorContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#power.
    def visitPower(self, ctx:ExprParser.PowerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#await_primary.
    def visitAwait_primary(self, ctx:ExprParser.Await_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#primary.
    def visitPrimary(self, ctx:ExprParser.PrimaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#slices.
    def visitSlices(self, ctx:ExprParser.SlicesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#slice.
    def visitSlice(self, ctx:ExprParser.SliceContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#atom.
    def visitAtom(self, ctx:ExprParser.AtomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#group.
    def visitGroup(self, ctx:ExprParser.GroupContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambdef.
    def visitLambdef(self, ctx:ExprParser.LambdefContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambda_params.
    def visitLambda_params(self, ctx:ExprParser.Lambda_paramsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambda_parameters.
    def visitLambda_parameters(self, ctx:ExprParser.Lambda_parametersContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambda_slash_no_default.
    def visitLambda_slash_no_default(self, ctx:ExprParser.Lambda_slash_no_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambda_slash_with_default.
    def visitLambda_slash_with_default(self, ctx:ExprParser.Lambda_slash_with_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambda_star_etc.
    def visitLambda_star_etc(self, ctx:ExprParser.Lambda_star_etcContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambda_kwds.
    def visitLambda_kwds(self, ctx:ExprParser.Lambda_kwdsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambda_param_no_default.
    def visitLambda_param_no_default(self, ctx:ExprParser.Lambda_param_no_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambda_param_with_default.
    def visitLambda_param_with_default(self, ctx:ExprParser.Lambda_param_with_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambda_param_maybe_default.
    def visitLambda_param_maybe_default(self, ctx:ExprParser.Lambda_param_maybe_defaultContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#lambda_param.
    def visitLambda_param(self, ctx:ExprParser.Lambda_paramContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fstring_middle.
    def visitFstring_middle(self, ctx:ExprParser.Fstring_middleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fstring_replacement_field.
    def visitFstring_replacement_field(self, ctx:ExprParser.Fstring_replacement_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fstring_conversion.
    def visitFstring_conversion(self, ctx:ExprParser.Fstring_conversionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fstring_full_format_spec.
    def visitFstring_full_format_spec(self, ctx:ExprParser.Fstring_full_format_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fstring_format_spec.
    def visitFstring_format_spec(self, ctx:ExprParser.Fstring_format_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#fstring.
    def visitFstring(self, ctx:ExprParser.FstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tstring_format_spec_replacement_field.
    def visitTstring_format_spec_replacement_field(self, ctx:ExprParser.Tstring_format_spec_replacement_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tstring_format_spec.
    def visitTstring_format_spec(self, ctx:ExprParser.Tstring_format_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tstring_full_format_spec.
    def visitTstring_full_format_spec(self, ctx:ExprParser.Tstring_full_format_specContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tstring_replacement_field.
    def visitTstring_replacement_field(self, ctx:ExprParser.Tstring_replacement_fieldContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tstring_middle.
    def visitTstring_middle(self, ctx:ExprParser.Tstring_middleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tstring.
    def visitTstring(self, ctx:ExprParser.TstringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#string.
    def visitString(self, ctx:ExprParser.StringContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#strings.
    def visitStrings(self, ctx:ExprParser.StringsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#list.
    def visitList(self, ctx:ExprParser.ListContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#tuple.
    def visitTuple(self, ctx:ExprParser.TupleContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#set.
    def visitSet(self, ctx:ExprParser.SetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#dict.
    def visitDict(self, ctx:ExprParser.DictContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#double_starred_kvpairs.
    def visitDouble_starred_kvpairs(self, ctx:ExprParser.Double_starred_kvpairsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#double_starred_kvpair.
    def visitDouble_starred_kvpair(self, ctx:ExprParser.Double_starred_kvpairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#kvpair.
    def visitKvpair(self, ctx:ExprParser.KvpairContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#for_if_clauses.
    def visitFor_if_clauses(self, ctx:ExprParser.For_if_clausesContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#for_if_clause.
    def visitFor_if_clause(self, ctx:ExprParser.For_if_clauseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#listcomp.
    def visitListcomp(self, ctx:ExprParser.ListcompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#setcomp.
    def visitSetcomp(self, ctx:ExprParser.SetcompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#genexp.
    def visitGenexp(self, ctx:ExprParser.GenexpContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#dictcomp.
    def visitDictcomp(self, ctx:ExprParser.DictcompContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#arguments.
    def visitArguments(self, ctx:ExprParser.ArgumentsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#args.
    def visitArgs(self, ctx:ExprParser.ArgsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#kwargs.
    def visitKwargs(self, ctx:ExprParser.KwargsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#starred_expression.
    def visitStarred_expression(self, ctx:ExprParser.Starred_expressionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#kwarg_or_starred.
    def visitKwarg_or_starred(self, ctx:ExprParser.Kwarg_or_starredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#kwarg_or_double_starred.
    def visitKwarg_or_double_starred(self, ctx:ExprParser.Kwarg_or_double_starredContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_targets.
    def visitStar_targets(self, ctx:ExprParser.Star_targetsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_targets_list_seq.
    def visitStar_targets_list_seq(self, ctx:ExprParser.Star_targets_list_seqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_targets_tuple_seq.
    def visitStar_targets_tuple_seq(self, ctx:ExprParser.Star_targets_tuple_seqContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_target.
    def visitStar_target(self, ctx:ExprParser.Star_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#target_with_star_atom.
    def visitTarget_with_star_atom(self, ctx:ExprParser.Target_with_star_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#star_atom.
    def visitStar_atom(self, ctx:ExprParser.Star_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#single_target.
    def visitSingle_target(self, ctx:ExprParser.Single_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#single_subscript_attribute_target.
    def visitSingle_subscript_attribute_target(self, ctx:ExprParser.Single_subscript_attribute_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#t_primary.
    def visitT_primary(self, ctx:ExprParser.T_primaryContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#t_lookahead.
    def visitT_lookahead(self, ctx:ExprParser.T_lookaheadContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#del_targets.
    def visitDel_targets(self, ctx:ExprParser.Del_targetsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#del_target.
    def visitDel_target(self, ctx:ExprParser.Del_targetContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#del_t_atom.
    def visitDel_t_atom(self, ctx:ExprParser.Del_t_atomContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#type_expressions.
    def visitType_expressions(self, ctx:ExprParser.Type_expressionsContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by ExprParser#func_type_comment.
    def visitFunc_type_comment(self, ctx:ExprParser.Func_type_commentContext):
        return self.visitChildren(ctx)



del ExprParser