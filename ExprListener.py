# Generated from ./Expr.g4 by ANTLR 4.13.2
from antlr4 import *
if "." in __name__:
    from .ExprParser import ExprParser
else:
    from ExprParser import ExprParser

# This class defines a complete listener for a parse tree produced by ExprParser.
class ExprListener(ParseTreeListener):

    # Enter a parse tree produced by ExprParser#file_.
    def enterFile_(self, ctx:ExprParser.File_Context):
        pass

    # Exit a parse tree produced by ExprParser#file_.
    def exitFile_(self, ctx:ExprParser.File_Context):
        pass


    # Enter a parse tree produced by ExprParser#interactive.
    def enterInteractive(self, ctx:ExprParser.InteractiveContext):
        pass

    # Exit a parse tree produced by ExprParser#interactive.
    def exitInteractive(self, ctx:ExprParser.InteractiveContext):
        pass


    # Enter a parse tree produced by ExprParser#eval_.
    def enterEval_(self, ctx:ExprParser.Eval_Context):
        pass

    # Exit a parse tree produced by ExprParser#eval_.
    def exitEval_(self, ctx:ExprParser.Eval_Context):
        pass


    # Enter a parse tree produced by ExprParser#func_type.
    def enterFunc_type(self, ctx:ExprParser.Func_typeContext):
        pass

    # Exit a parse tree produced by ExprParser#func_type.
    def exitFunc_type(self, ctx:ExprParser.Func_typeContext):
        pass


    # Enter a parse tree produced by ExprParser#statements.
    def enterStatements(self, ctx:ExprParser.StatementsContext):
        pass

    # Exit a parse tree produced by ExprParser#statements.
    def exitStatements(self, ctx:ExprParser.StatementsContext):
        pass


    # Enter a parse tree produced by ExprParser#statement.
    def enterStatement(self, ctx:ExprParser.StatementContext):
        pass

    # Exit a parse tree produced by ExprParser#statement.
    def exitStatement(self, ctx:ExprParser.StatementContext):
        pass


    # Enter a parse tree produced by ExprParser#single_compound_stmt.
    def enterSingle_compound_stmt(self, ctx:ExprParser.Single_compound_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#single_compound_stmt.
    def exitSingle_compound_stmt(self, ctx:ExprParser.Single_compound_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#statement_newline.
    def enterStatement_newline(self, ctx:ExprParser.Statement_newlineContext):
        pass

    # Exit a parse tree produced by ExprParser#statement_newline.
    def exitStatement_newline(self, ctx:ExprParser.Statement_newlineContext):
        pass


    # Enter a parse tree produced by ExprParser#simple_stmts.
    def enterSimple_stmts(self, ctx:ExprParser.Simple_stmtsContext):
        pass

    # Exit a parse tree produced by ExprParser#simple_stmts.
    def exitSimple_stmts(self, ctx:ExprParser.Simple_stmtsContext):
        pass


    # Enter a parse tree produced by ExprParser#simple_stmt.
    def enterSimple_stmt(self, ctx:ExprParser.Simple_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#simple_stmt.
    def exitSimple_stmt(self, ctx:ExprParser.Simple_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#compound_stmt.
    def enterCompound_stmt(self, ctx:ExprParser.Compound_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#compound_stmt.
    def exitCompound_stmt(self, ctx:ExprParser.Compound_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment.
    def enterAssignment(self, ctx:ExprParser.AssignmentContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment.
    def exitAssignment(self, ctx:ExprParser.AssignmentContext):
        pass


    # Enter a parse tree produced by ExprParser#annotated_rhs.
    def enterAnnotated_rhs(self, ctx:ExprParser.Annotated_rhsContext):
        pass

    # Exit a parse tree produced by ExprParser#annotated_rhs.
    def exitAnnotated_rhs(self, ctx:ExprParser.Annotated_rhsContext):
        pass


    # Enter a parse tree produced by ExprParser#augassign.
    def enterAugassign(self, ctx:ExprParser.AugassignContext):
        pass

    # Exit a parse tree produced by ExprParser#augassign.
    def exitAugassign(self, ctx:ExprParser.AugassignContext):
        pass


    # Enter a parse tree produced by ExprParser#return_stmt.
    def enterReturn_stmt(self, ctx:ExprParser.Return_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#return_stmt.
    def exitReturn_stmt(self, ctx:ExprParser.Return_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#raise_stmt.
    def enterRaise_stmt(self, ctx:ExprParser.Raise_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#raise_stmt.
    def exitRaise_stmt(self, ctx:ExprParser.Raise_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#pass_stmt.
    def enterPass_stmt(self, ctx:ExprParser.Pass_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#pass_stmt.
    def exitPass_stmt(self, ctx:ExprParser.Pass_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#break_stmt.
    def enterBreak_stmt(self, ctx:ExprParser.Break_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#break_stmt.
    def exitBreak_stmt(self, ctx:ExprParser.Break_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#continue_stmt.
    def enterContinue_stmt(self, ctx:ExprParser.Continue_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#continue_stmt.
    def exitContinue_stmt(self, ctx:ExprParser.Continue_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#global_stmt.
    def enterGlobal_stmt(self, ctx:ExprParser.Global_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#global_stmt.
    def exitGlobal_stmt(self, ctx:ExprParser.Global_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#nonlocal_stmt.
    def enterNonlocal_stmt(self, ctx:ExprParser.Nonlocal_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#nonlocal_stmt.
    def exitNonlocal_stmt(self, ctx:ExprParser.Nonlocal_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#del_stmt.
    def enterDel_stmt(self, ctx:ExprParser.Del_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#del_stmt.
    def exitDel_stmt(self, ctx:ExprParser.Del_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#yield_stmt.
    def enterYield_stmt(self, ctx:ExprParser.Yield_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#yield_stmt.
    def exitYield_stmt(self, ctx:ExprParser.Yield_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#assert_stmt.
    def enterAssert_stmt(self, ctx:ExprParser.Assert_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#assert_stmt.
    def exitAssert_stmt(self, ctx:ExprParser.Assert_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#import_stmt.
    def enterImport_stmt(self, ctx:ExprParser.Import_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#import_stmt.
    def exitImport_stmt(self, ctx:ExprParser.Import_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#import_name.
    def enterImport_name(self, ctx:ExprParser.Import_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#import_name.
    def exitImport_name(self, ctx:ExprParser.Import_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#import_from.
    def enterImport_from(self, ctx:ExprParser.Import_fromContext):
        pass

    # Exit a parse tree produced by ExprParser#import_from.
    def exitImport_from(self, ctx:ExprParser.Import_fromContext):
        pass


    # Enter a parse tree produced by ExprParser#import_from_targets.
    def enterImport_from_targets(self, ctx:ExprParser.Import_from_targetsContext):
        pass

    # Exit a parse tree produced by ExprParser#import_from_targets.
    def exitImport_from_targets(self, ctx:ExprParser.Import_from_targetsContext):
        pass


    # Enter a parse tree produced by ExprParser#import_from_as_names.
    def enterImport_from_as_names(self, ctx:ExprParser.Import_from_as_namesContext):
        pass

    # Exit a parse tree produced by ExprParser#import_from_as_names.
    def exitImport_from_as_names(self, ctx:ExprParser.Import_from_as_namesContext):
        pass


    # Enter a parse tree produced by ExprParser#import_from_as_name.
    def enterImport_from_as_name(self, ctx:ExprParser.Import_from_as_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#import_from_as_name.
    def exitImport_from_as_name(self, ctx:ExprParser.Import_from_as_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#dotted_as_names.
    def enterDotted_as_names(self, ctx:ExprParser.Dotted_as_namesContext):
        pass

    # Exit a parse tree produced by ExprParser#dotted_as_names.
    def exitDotted_as_names(self, ctx:ExprParser.Dotted_as_namesContext):
        pass


    # Enter a parse tree produced by ExprParser#dotted_as_name.
    def enterDotted_as_name(self, ctx:ExprParser.Dotted_as_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#dotted_as_name.
    def exitDotted_as_name(self, ctx:ExprParser.Dotted_as_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#dotted_name.
    def enterDotted_name(self, ctx:ExprParser.Dotted_nameContext):
        pass

    # Exit a parse tree produced by ExprParser#dotted_name.
    def exitDotted_name(self, ctx:ExprParser.Dotted_nameContext):
        pass


    # Enter a parse tree produced by ExprParser#block.
    def enterBlock(self, ctx:ExprParser.BlockContext):
        pass

    # Exit a parse tree produced by ExprParser#block.
    def exitBlock(self, ctx:ExprParser.BlockContext):
        pass


    # Enter a parse tree produced by ExprParser#decorators.
    def enterDecorators(self, ctx:ExprParser.DecoratorsContext):
        pass

    # Exit a parse tree produced by ExprParser#decorators.
    def exitDecorators(self, ctx:ExprParser.DecoratorsContext):
        pass


    # Enter a parse tree produced by ExprParser#class_def.
    def enterClass_def(self, ctx:ExprParser.Class_defContext):
        pass

    # Exit a parse tree produced by ExprParser#class_def.
    def exitClass_def(self, ctx:ExprParser.Class_defContext):
        pass


    # Enter a parse tree produced by ExprParser#class_def_raw.
    def enterClass_def_raw(self, ctx:ExprParser.Class_def_rawContext):
        pass

    # Exit a parse tree produced by ExprParser#class_def_raw.
    def exitClass_def_raw(self, ctx:ExprParser.Class_def_rawContext):
        pass


    # Enter a parse tree produced by ExprParser#function_def.
    def enterFunction_def(self, ctx:ExprParser.Function_defContext):
        pass

    # Exit a parse tree produced by ExprParser#function_def.
    def exitFunction_def(self, ctx:ExprParser.Function_defContext):
        pass


    # Enter a parse tree produced by ExprParser#function_def_raw.
    def enterFunction_def_raw(self, ctx:ExprParser.Function_def_rawContext):
        pass

    # Exit a parse tree produced by ExprParser#function_def_raw.
    def exitFunction_def_raw(self, ctx:ExprParser.Function_def_rawContext):
        pass


    # Enter a parse tree produced by ExprParser#params.
    def enterParams(self, ctx:ExprParser.ParamsContext):
        pass

    # Exit a parse tree produced by ExprParser#params.
    def exitParams(self, ctx:ExprParser.ParamsContext):
        pass


    # Enter a parse tree produced by ExprParser#parameters.
    def enterParameters(self, ctx:ExprParser.ParametersContext):
        pass

    # Exit a parse tree produced by ExprParser#parameters.
    def exitParameters(self, ctx:ExprParser.ParametersContext):
        pass


    # Enter a parse tree produced by ExprParser#slash_no_default.
    def enterSlash_no_default(self, ctx:ExprParser.Slash_no_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#slash_no_default.
    def exitSlash_no_default(self, ctx:ExprParser.Slash_no_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#slash_with_default.
    def enterSlash_with_default(self, ctx:ExprParser.Slash_with_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#slash_with_default.
    def exitSlash_with_default(self, ctx:ExprParser.Slash_with_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#star_etc.
    def enterStar_etc(self, ctx:ExprParser.Star_etcContext):
        pass

    # Exit a parse tree produced by ExprParser#star_etc.
    def exitStar_etc(self, ctx:ExprParser.Star_etcContext):
        pass


    # Enter a parse tree produced by ExprParser#kwds.
    def enterKwds(self, ctx:ExprParser.KwdsContext):
        pass

    # Exit a parse tree produced by ExprParser#kwds.
    def exitKwds(self, ctx:ExprParser.KwdsContext):
        pass


    # Enter a parse tree produced by ExprParser#param_no_default.
    def enterParam_no_default(self, ctx:ExprParser.Param_no_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#param_no_default.
    def exitParam_no_default(self, ctx:ExprParser.Param_no_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#param_no_default_star_annotation.
    def enterParam_no_default_star_annotation(self, ctx:ExprParser.Param_no_default_star_annotationContext):
        pass

    # Exit a parse tree produced by ExprParser#param_no_default_star_annotation.
    def exitParam_no_default_star_annotation(self, ctx:ExprParser.Param_no_default_star_annotationContext):
        pass


    # Enter a parse tree produced by ExprParser#param_with_default.
    def enterParam_with_default(self, ctx:ExprParser.Param_with_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#param_with_default.
    def exitParam_with_default(self, ctx:ExprParser.Param_with_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#param_maybe_default.
    def enterParam_maybe_default(self, ctx:ExprParser.Param_maybe_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#param_maybe_default.
    def exitParam_maybe_default(self, ctx:ExprParser.Param_maybe_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#param.
    def enterParam(self, ctx:ExprParser.ParamContext):
        pass

    # Exit a parse tree produced by ExprParser#param.
    def exitParam(self, ctx:ExprParser.ParamContext):
        pass


    # Enter a parse tree produced by ExprParser#param_star_annotation.
    def enterParam_star_annotation(self, ctx:ExprParser.Param_star_annotationContext):
        pass

    # Exit a parse tree produced by ExprParser#param_star_annotation.
    def exitParam_star_annotation(self, ctx:ExprParser.Param_star_annotationContext):
        pass


    # Enter a parse tree produced by ExprParser#annotation.
    def enterAnnotation(self, ctx:ExprParser.AnnotationContext):
        pass

    # Exit a parse tree produced by ExprParser#annotation.
    def exitAnnotation(self, ctx:ExprParser.AnnotationContext):
        pass


    # Enter a parse tree produced by ExprParser#star_annotation.
    def enterStar_annotation(self, ctx:ExprParser.Star_annotationContext):
        pass

    # Exit a parse tree produced by ExprParser#star_annotation.
    def exitStar_annotation(self, ctx:ExprParser.Star_annotationContext):
        pass


    # Enter a parse tree produced by ExprParser#default.
    def enterDefault(self, ctx:ExprParser.DefaultContext):
        pass

    # Exit a parse tree produced by ExprParser#default.
    def exitDefault(self, ctx:ExprParser.DefaultContext):
        pass


    # Enter a parse tree produced by ExprParser#if_stmt.
    def enterIf_stmt(self, ctx:ExprParser.If_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#if_stmt.
    def exitIf_stmt(self, ctx:ExprParser.If_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#elif_stmt.
    def enterElif_stmt(self, ctx:ExprParser.Elif_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#elif_stmt.
    def exitElif_stmt(self, ctx:ExprParser.Elif_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#else_block.
    def enterElse_block(self, ctx:ExprParser.Else_blockContext):
        pass

    # Exit a parse tree produced by ExprParser#else_block.
    def exitElse_block(self, ctx:ExprParser.Else_blockContext):
        pass


    # Enter a parse tree produced by ExprParser#while_stmt.
    def enterWhile_stmt(self, ctx:ExprParser.While_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#while_stmt.
    def exitWhile_stmt(self, ctx:ExprParser.While_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#for_stmt.
    def enterFor_stmt(self, ctx:ExprParser.For_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#for_stmt.
    def exitFor_stmt(self, ctx:ExprParser.For_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#with_stmt.
    def enterWith_stmt(self, ctx:ExprParser.With_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#with_stmt.
    def exitWith_stmt(self, ctx:ExprParser.With_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#with_item.
    def enterWith_item(self, ctx:ExprParser.With_itemContext):
        pass

    # Exit a parse tree produced by ExprParser#with_item.
    def exitWith_item(self, ctx:ExprParser.With_itemContext):
        pass


    # Enter a parse tree produced by ExprParser#try_stmt.
    def enterTry_stmt(self, ctx:ExprParser.Try_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#try_stmt.
    def exitTry_stmt(self, ctx:ExprParser.Try_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#except_block.
    def enterExcept_block(self, ctx:ExprParser.Except_blockContext):
        pass

    # Exit a parse tree produced by ExprParser#except_block.
    def exitExcept_block(self, ctx:ExprParser.Except_blockContext):
        pass


    # Enter a parse tree produced by ExprParser#except_star_block.
    def enterExcept_star_block(self, ctx:ExprParser.Except_star_blockContext):
        pass

    # Exit a parse tree produced by ExprParser#except_star_block.
    def exitExcept_star_block(self, ctx:ExprParser.Except_star_blockContext):
        pass


    # Enter a parse tree produced by ExprParser#finally_block.
    def enterFinally_block(self, ctx:ExprParser.Finally_blockContext):
        pass

    # Exit a parse tree produced by ExprParser#finally_block.
    def exitFinally_block(self, ctx:ExprParser.Finally_blockContext):
        pass


    # Enter a parse tree produced by ExprParser#match_stmt.
    def enterMatch_stmt(self, ctx:ExprParser.Match_stmtContext):
        pass

    # Exit a parse tree produced by ExprParser#match_stmt.
    def exitMatch_stmt(self, ctx:ExprParser.Match_stmtContext):
        pass


    # Enter a parse tree produced by ExprParser#subject_expr.
    def enterSubject_expr(self, ctx:ExprParser.Subject_exprContext):
        pass

    # Exit a parse tree produced by ExprParser#subject_expr.
    def exitSubject_expr(self, ctx:ExprParser.Subject_exprContext):
        pass


    # Enter a parse tree produced by ExprParser#case_block.
    def enterCase_block(self, ctx:ExprParser.Case_blockContext):
        pass

    # Exit a parse tree produced by ExprParser#case_block.
    def exitCase_block(self, ctx:ExprParser.Case_blockContext):
        pass


    # Enter a parse tree produced by ExprParser#guard.
    def enterGuard(self, ctx:ExprParser.GuardContext):
        pass

    # Exit a parse tree produced by ExprParser#guard.
    def exitGuard(self, ctx:ExprParser.GuardContext):
        pass


    # Enter a parse tree produced by ExprParser#patterns.
    def enterPatterns(self, ctx:ExprParser.PatternsContext):
        pass

    # Exit a parse tree produced by ExprParser#patterns.
    def exitPatterns(self, ctx:ExprParser.PatternsContext):
        pass


    # Enter a parse tree produced by ExprParser#pattern.
    def enterPattern(self, ctx:ExprParser.PatternContext):
        pass

    # Exit a parse tree produced by ExprParser#pattern.
    def exitPattern(self, ctx:ExprParser.PatternContext):
        pass


    # Enter a parse tree produced by ExprParser#as_pattern.
    def enterAs_pattern(self, ctx:ExprParser.As_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#as_pattern.
    def exitAs_pattern(self, ctx:ExprParser.As_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#or_pattern.
    def enterOr_pattern(self, ctx:ExprParser.Or_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#or_pattern.
    def exitOr_pattern(self, ctx:ExprParser.Or_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#closed_pattern.
    def enterClosed_pattern(self, ctx:ExprParser.Closed_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#closed_pattern.
    def exitClosed_pattern(self, ctx:ExprParser.Closed_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#literal_pattern.
    def enterLiteral_pattern(self, ctx:ExprParser.Literal_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#literal_pattern.
    def exitLiteral_pattern(self, ctx:ExprParser.Literal_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#literal_expr.
    def enterLiteral_expr(self, ctx:ExprParser.Literal_exprContext):
        pass

    # Exit a parse tree produced by ExprParser#literal_expr.
    def exitLiteral_expr(self, ctx:ExprParser.Literal_exprContext):
        pass


    # Enter a parse tree produced by ExprParser#complex_number.
    def enterComplex_number(self, ctx:ExprParser.Complex_numberContext):
        pass

    # Exit a parse tree produced by ExprParser#complex_number.
    def exitComplex_number(self, ctx:ExprParser.Complex_numberContext):
        pass


    # Enter a parse tree produced by ExprParser#signed_number.
    def enterSigned_number(self, ctx:ExprParser.Signed_numberContext):
        pass

    # Exit a parse tree produced by ExprParser#signed_number.
    def exitSigned_number(self, ctx:ExprParser.Signed_numberContext):
        pass


    # Enter a parse tree produced by ExprParser#signed_real_number.
    def enterSigned_real_number(self, ctx:ExprParser.Signed_real_numberContext):
        pass

    # Exit a parse tree produced by ExprParser#signed_real_number.
    def exitSigned_real_number(self, ctx:ExprParser.Signed_real_numberContext):
        pass


    # Enter a parse tree produced by ExprParser#real_number.
    def enterReal_number(self, ctx:ExprParser.Real_numberContext):
        pass

    # Exit a parse tree produced by ExprParser#real_number.
    def exitReal_number(self, ctx:ExprParser.Real_numberContext):
        pass


    # Enter a parse tree produced by ExprParser#imaginary_number.
    def enterImaginary_number(self, ctx:ExprParser.Imaginary_numberContext):
        pass

    # Exit a parse tree produced by ExprParser#imaginary_number.
    def exitImaginary_number(self, ctx:ExprParser.Imaginary_numberContext):
        pass


    # Enter a parse tree produced by ExprParser#capture_pattern.
    def enterCapture_pattern(self, ctx:ExprParser.Capture_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#capture_pattern.
    def exitCapture_pattern(self, ctx:ExprParser.Capture_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#pattern_capture_target.
    def enterPattern_capture_target(self, ctx:ExprParser.Pattern_capture_targetContext):
        pass

    # Exit a parse tree produced by ExprParser#pattern_capture_target.
    def exitPattern_capture_target(self, ctx:ExprParser.Pattern_capture_targetContext):
        pass


    # Enter a parse tree produced by ExprParser#wildcard_pattern.
    def enterWildcard_pattern(self, ctx:ExprParser.Wildcard_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#wildcard_pattern.
    def exitWildcard_pattern(self, ctx:ExprParser.Wildcard_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#value_pattern.
    def enterValue_pattern(self, ctx:ExprParser.Value_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#value_pattern.
    def exitValue_pattern(self, ctx:ExprParser.Value_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#attr.
    def enterAttr(self, ctx:ExprParser.AttrContext):
        pass

    # Exit a parse tree produced by ExprParser#attr.
    def exitAttr(self, ctx:ExprParser.AttrContext):
        pass


    # Enter a parse tree produced by ExprParser#name_or_attr.
    def enterName_or_attr(self, ctx:ExprParser.Name_or_attrContext):
        pass

    # Exit a parse tree produced by ExprParser#name_or_attr.
    def exitName_or_attr(self, ctx:ExprParser.Name_or_attrContext):
        pass


    # Enter a parse tree produced by ExprParser#group_pattern.
    def enterGroup_pattern(self, ctx:ExprParser.Group_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#group_pattern.
    def exitGroup_pattern(self, ctx:ExprParser.Group_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#sequence_pattern.
    def enterSequence_pattern(self, ctx:ExprParser.Sequence_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#sequence_pattern.
    def exitSequence_pattern(self, ctx:ExprParser.Sequence_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#open_sequence_pattern.
    def enterOpen_sequence_pattern(self, ctx:ExprParser.Open_sequence_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#open_sequence_pattern.
    def exitOpen_sequence_pattern(self, ctx:ExprParser.Open_sequence_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#maybe_sequence_pattern.
    def enterMaybe_sequence_pattern(self, ctx:ExprParser.Maybe_sequence_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#maybe_sequence_pattern.
    def exitMaybe_sequence_pattern(self, ctx:ExprParser.Maybe_sequence_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#maybe_star_pattern.
    def enterMaybe_star_pattern(self, ctx:ExprParser.Maybe_star_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#maybe_star_pattern.
    def exitMaybe_star_pattern(self, ctx:ExprParser.Maybe_star_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#star_pattern.
    def enterStar_pattern(self, ctx:ExprParser.Star_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#star_pattern.
    def exitStar_pattern(self, ctx:ExprParser.Star_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#mapping_pattern.
    def enterMapping_pattern(self, ctx:ExprParser.Mapping_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#mapping_pattern.
    def exitMapping_pattern(self, ctx:ExprParser.Mapping_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#items_pattern.
    def enterItems_pattern(self, ctx:ExprParser.Items_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#items_pattern.
    def exitItems_pattern(self, ctx:ExprParser.Items_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#key_value_pattern.
    def enterKey_value_pattern(self, ctx:ExprParser.Key_value_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#key_value_pattern.
    def exitKey_value_pattern(self, ctx:ExprParser.Key_value_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#double_star_pattern.
    def enterDouble_star_pattern(self, ctx:ExprParser.Double_star_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#double_star_pattern.
    def exitDouble_star_pattern(self, ctx:ExprParser.Double_star_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#class_pattern.
    def enterClass_pattern(self, ctx:ExprParser.Class_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#class_pattern.
    def exitClass_pattern(self, ctx:ExprParser.Class_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#positional_patterns.
    def enterPositional_patterns(self, ctx:ExprParser.Positional_patternsContext):
        pass

    # Exit a parse tree produced by ExprParser#positional_patterns.
    def exitPositional_patterns(self, ctx:ExprParser.Positional_patternsContext):
        pass


    # Enter a parse tree produced by ExprParser#keyword_patterns.
    def enterKeyword_patterns(self, ctx:ExprParser.Keyword_patternsContext):
        pass

    # Exit a parse tree produced by ExprParser#keyword_patterns.
    def exitKeyword_patterns(self, ctx:ExprParser.Keyword_patternsContext):
        pass


    # Enter a parse tree produced by ExprParser#keyword_pattern.
    def enterKeyword_pattern(self, ctx:ExprParser.Keyword_patternContext):
        pass

    # Exit a parse tree produced by ExprParser#keyword_pattern.
    def exitKeyword_pattern(self, ctx:ExprParser.Keyword_patternContext):
        pass


    # Enter a parse tree produced by ExprParser#type_alias.
    def enterType_alias(self, ctx:ExprParser.Type_aliasContext):
        pass

    # Exit a parse tree produced by ExprParser#type_alias.
    def exitType_alias(self, ctx:ExprParser.Type_aliasContext):
        pass


    # Enter a parse tree produced by ExprParser#type_params.
    def enterType_params(self, ctx:ExprParser.Type_paramsContext):
        pass

    # Exit a parse tree produced by ExprParser#type_params.
    def exitType_params(self, ctx:ExprParser.Type_paramsContext):
        pass


    # Enter a parse tree produced by ExprParser#type_param_seq.
    def enterType_param_seq(self, ctx:ExprParser.Type_param_seqContext):
        pass

    # Exit a parse tree produced by ExprParser#type_param_seq.
    def exitType_param_seq(self, ctx:ExprParser.Type_param_seqContext):
        pass


    # Enter a parse tree produced by ExprParser#type_param.
    def enterType_param(self, ctx:ExprParser.Type_paramContext):
        pass

    # Exit a parse tree produced by ExprParser#type_param.
    def exitType_param(self, ctx:ExprParser.Type_paramContext):
        pass


    # Enter a parse tree produced by ExprParser#type_param_bound.
    def enterType_param_bound(self, ctx:ExprParser.Type_param_boundContext):
        pass

    # Exit a parse tree produced by ExprParser#type_param_bound.
    def exitType_param_bound(self, ctx:ExprParser.Type_param_boundContext):
        pass


    # Enter a parse tree produced by ExprParser#type_param_default.
    def enterType_param_default(self, ctx:ExprParser.Type_param_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#type_param_default.
    def exitType_param_default(self, ctx:ExprParser.Type_param_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#type_param_starred_default.
    def enterType_param_starred_default(self, ctx:ExprParser.Type_param_starred_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#type_param_starred_default.
    def exitType_param_starred_default(self, ctx:ExprParser.Type_param_starred_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#expressions.
    def enterExpressions(self, ctx:ExprParser.ExpressionsContext):
        pass

    # Exit a parse tree produced by ExprParser#expressions.
    def exitExpressions(self, ctx:ExprParser.ExpressionsContext):
        pass


    # Enter a parse tree produced by ExprParser#expression.
    def enterExpression(self, ctx:ExprParser.ExpressionContext):
        pass

    # Exit a parse tree produced by ExprParser#expression.
    def exitExpression(self, ctx:ExprParser.ExpressionContext):
        pass


    # Enter a parse tree produced by ExprParser#yield_expr.
    def enterYield_expr(self, ctx:ExprParser.Yield_exprContext):
        pass

    # Exit a parse tree produced by ExprParser#yield_expr.
    def exitYield_expr(self, ctx:ExprParser.Yield_exprContext):
        pass


    # Enter a parse tree produced by ExprParser#star_expressions.
    def enterStar_expressions(self, ctx:ExprParser.Star_expressionsContext):
        pass

    # Exit a parse tree produced by ExprParser#star_expressions.
    def exitStar_expressions(self, ctx:ExprParser.Star_expressionsContext):
        pass


    # Enter a parse tree produced by ExprParser#star_expression.
    def enterStar_expression(self, ctx:ExprParser.Star_expressionContext):
        pass

    # Exit a parse tree produced by ExprParser#star_expression.
    def exitStar_expression(self, ctx:ExprParser.Star_expressionContext):
        pass


    # Enter a parse tree produced by ExprParser#star_named_expressions.
    def enterStar_named_expressions(self, ctx:ExprParser.Star_named_expressionsContext):
        pass

    # Exit a parse tree produced by ExprParser#star_named_expressions.
    def exitStar_named_expressions(self, ctx:ExprParser.Star_named_expressionsContext):
        pass


    # Enter a parse tree produced by ExprParser#star_named_expression.
    def enterStar_named_expression(self, ctx:ExprParser.Star_named_expressionContext):
        pass

    # Exit a parse tree produced by ExprParser#star_named_expression.
    def exitStar_named_expression(self, ctx:ExprParser.Star_named_expressionContext):
        pass


    # Enter a parse tree produced by ExprParser#assignment_expression.
    def enterAssignment_expression(self, ctx:ExprParser.Assignment_expressionContext):
        pass

    # Exit a parse tree produced by ExprParser#assignment_expression.
    def exitAssignment_expression(self, ctx:ExprParser.Assignment_expressionContext):
        pass


    # Enter a parse tree produced by ExprParser#named_expression.
    def enterNamed_expression(self, ctx:ExprParser.Named_expressionContext):
        pass

    # Exit a parse tree produced by ExprParser#named_expression.
    def exitNamed_expression(self, ctx:ExprParser.Named_expressionContext):
        pass


    # Enter a parse tree produced by ExprParser#disjunction.
    def enterDisjunction(self, ctx:ExprParser.DisjunctionContext):
        pass

    # Exit a parse tree produced by ExprParser#disjunction.
    def exitDisjunction(self, ctx:ExprParser.DisjunctionContext):
        pass


    # Enter a parse tree produced by ExprParser#conjunction.
    def enterConjunction(self, ctx:ExprParser.ConjunctionContext):
        pass

    # Exit a parse tree produced by ExprParser#conjunction.
    def exitConjunction(self, ctx:ExprParser.ConjunctionContext):
        pass


    # Enter a parse tree produced by ExprParser#inversion.
    def enterInversion(self, ctx:ExprParser.InversionContext):
        pass

    # Exit a parse tree produced by ExprParser#inversion.
    def exitInversion(self, ctx:ExprParser.InversionContext):
        pass


    # Enter a parse tree produced by ExprParser#comparison.
    def enterComparison(self, ctx:ExprParser.ComparisonContext):
        pass

    # Exit a parse tree produced by ExprParser#comparison.
    def exitComparison(self, ctx:ExprParser.ComparisonContext):
        pass


    # Enter a parse tree produced by ExprParser#compare_op_bitwise_or_pair.
    def enterCompare_op_bitwise_or_pair(self, ctx:ExprParser.Compare_op_bitwise_or_pairContext):
        pass

    # Exit a parse tree produced by ExprParser#compare_op_bitwise_or_pair.
    def exitCompare_op_bitwise_or_pair(self, ctx:ExprParser.Compare_op_bitwise_or_pairContext):
        pass


    # Enter a parse tree produced by ExprParser#eq_bitwise_or.
    def enterEq_bitwise_or(self, ctx:ExprParser.Eq_bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#eq_bitwise_or.
    def exitEq_bitwise_or(self, ctx:ExprParser.Eq_bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#noteq_bitwise_or.
    def enterNoteq_bitwise_or(self, ctx:ExprParser.Noteq_bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#noteq_bitwise_or.
    def exitNoteq_bitwise_or(self, ctx:ExprParser.Noteq_bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#lte_bitwise_or.
    def enterLte_bitwise_or(self, ctx:ExprParser.Lte_bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#lte_bitwise_or.
    def exitLte_bitwise_or(self, ctx:ExprParser.Lte_bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#lt_bitwise_or.
    def enterLt_bitwise_or(self, ctx:ExprParser.Lt_bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#lt_bitwise_or.
    def exitLt_bitwise_or(self, ctx:ExprParser.Lt_bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#gte_bitwise_or.
    def enterGte_bitwise_or(self, ctx:ExprParser.Gte_bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#gte_bitwise_or.
    def exitGte_bitwise_or(self, ctx:ExprParser.Gte_bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#gt_bitwise_or.
    def enterGt_bitwise_or(self, ctx:ExprParser.Gt_bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#gt_bitwise_or.
    def exitGt_bitwise_or(self, ctx:ExprParser.Gt_bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#notin_bitwise_or.
    def enterNotin_bitwise_or(self, ctx:ExprParser.Notin_bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#notin_bitwise_or.
    def exitNotin_bitwise_or(self, ctx:ExprParser.Notin_bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#in_bitwise_or.
    def enterIn_bitwise_or(self, ctx:ExprParser.In_bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#in_bitwise_or.
    def exitIn_bitwise_or(self, ctx:ExprParser.In_bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#isnot_bitwise_or.
    def enterIsnot_bitwise_or(self, ctx:ExprParser.Isnot_bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#isnot_bitwise_or.
    def exitIsnot_bitwise_or(self, ctx:ExprParser.Isnot_bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#is_bitwise_or.
    def enterIs_bitwise_or(self, ctx:ExprParser.Is_bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#is_bitwise_or.
    def exitIs_bitwise_or(self, ctx:ExprParser.Is_bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#bitwise_or.
    def enterBitwise_or(self, ctx:ExprParser.Bitwise_orContext):
        pass

    # Exit a parse tree produced by ExprParser#bitwise_or.
    def exitBitwise_or(self, ctx:ExprParser.Bitwise_orContext):
        pass


    # Enter a parse tree produced by ExprParser#bitwise_xor.
    def enterBitwise_xor(self, ctx:ExprParser.Bitwise_xorContext):
        pass

    # Exit a parse tree produced by ExprParser#bitwise_xor.
    def exitBitwise_xor(self, ctx:ExprParser.Bitwise_xorContext):
        pass


    # Enter a parse tree produced by ExprParser#bitwise_and.
    def enterBitwise_and(self, ctx:ExprParser.Bitwise_andContext):
        pass

    # Exit a parse tree produced by ExprParser#bitwise_and.
    def exitBitwise_and(self, ctx:ExprParser.Bitwise_andContext):
        pass


    # Enter a parse tree produced by ExprParser#shift_expr.
    def enterShift_expr(self, ctx:ExprParser.Shift_exprContext):
        pass

    # Exit a parse tree produced by ExprParser#shift_expr.
    def exitShift_expr(self, ctx:ExprParser.Shift_exprContext):
        pass


    # Enter a parse tree produced by ExprParser#sum.
    def enterSum(self, ctx:ExprParser.SumContext):
        pass

    # Exit a parse tree produced by ExprParser#sum.
    def exitSum(self, ctx:ExprParser.SumContext):
        pass


    # Enter a parse tree produced by ExprParser#term.
    def enterTerm(self, ctx:ExprParser.TermContext):
        pass

    # Exit a parse tree produced by ExprParser#term.
    def exitTerm(self, ctx:ExprParser.TermContext):
        pass


    # Enter a parse tree produced by ExprParser#factor.
    def enterFactor(self, ctx:ExprParser.FactorContext):
        pass

    # Exit a parse tree produced by ExprParser#factor.
    def exitFactor(self, ctx:ExprParser.FactorContext):
        pass


    # Enter a parse tree produced by ExprParser#power.
    def enterPower(self, ctx:ExprParser.PowerContext):
        pass

    # Exit a parse tree produced by ExprParser#power.
    def exitPower(self, ctx:ExprParser.PowerContext):
        pass


    # Enter a parse tree produced by ExprParser#await_primary.
    def enterAwait_primary(self, ctx:ExprParser.Await_primaryContext):
        pass

    # Exit a parse tree produced by ExprParser#await_primary.
    def exitAwait_primary(self, ctx:ExprParser.Await_primaryContext):
        pass


    # Enter a parse tree produced by ExprParser#primary.
    def enterPrimary(self, ctx:ExprParser.PrimaryContext):
        pass

    # Exit a parse tree produced by ExprParser#primary.
    def exitPrimary(self, ctx:ExprParser.PrimaryContext):
        pass


    # Enter a parse tree produced by ExprParser#slices.
    def enterSlices(self, ctx:ExprParser.SlicesContext):
        pass

    # Exit a parse tree produced by ExprParser#slices.
    def exitSlices(self, ctx:ExprParser.SlicesContext):
        pass


    # Enter a parse tree produced by ExprParser#slice.
    def enterSlice(self, ctx:ExprParser.SliceContext):
        pass

    # Exit a parse tree produced by ExprParser#slice.
    def exitSlice(self, ctx:ExprParser.SliceContext):
        pass


    # Enter a parse tree produced by ExprParser#atom.
    def enterAtom(self, ctx:ExprParser.AtomContext):
        pass

    # Exit a parse tree produced by ExprParser#atom.
    def exitAtom(self, ctx:ExprParser.AtomContext):
        pass


    # Enter a parse tree produced by ExprParser#group.
    def enterGroup(self, ctx:ExprParser.GroupContext):
        pass

    # Exit a parse tree produced by ExprParser#group.
    def exitGroup(self, ctx:ExprParser.GroupContext):
        pass


    # Enter a parse tree produced by ExprParser#lambdef.
    def enterLambdef(self, ctx:ExprParser.LambdefContext):
        pass

    # Exit a parse tree produced by ExprParser#lambdef.
    def exitLambdef(self, ctx:ExprParser.LambdefContext):
        pass


    # Enter a parse tree produced by ExprParser#lambda_params.
    def enterLambda_params(self, ctx:ExprParser.Lambda_paramsContext):
        pass

    # Exit a parse tree produced by ExprParser#lambda_params.
    def exitLambda_params(self, ctx:ExprParser.Lambda_paramsContext):
        pass


    # Enter a parse tree produced by ExprParser#lambda_parameters.
    def enterLambda_parameters(self, ctx:ExprParser.Lambda_parametersContext):
        pass

    # Exit a parse tree produced by ExprParser#lambda_parameters.
    def exitLambda_parameters(self, ctx:ExprParser.Lambda_parametersContext):
        pass


    # Enter a parse tree produced by ExprParser#lambda_slash_no_default.
    def enterLambda_slash_no_default(self, ctx:ExprParser.Lambda_slash_no_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#lambda_slash_no_default.
    def exitLambda_slash_no_default(self, ctx:ExprParser.Lambda_slash_no_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#lambda_slash_with_default.
    def enterLambda_slash_with_default(self, ctx:ExprParser.Lambda_slash_with_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#lambda_slash_with_default.
    def exitLambda_slash_with_default(self, ctx:ExprParser.Lambda_slash_with_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#lambda_star_etc.
    def enterLambda_star_etc(self, ctx:ExprParser.Lambda_star_etcContext):
        pass

    # Exit a parse tree produced by ExprParser#lambda_star_etc.
    def exitLambda_star_etc(self, ctx:ExprParser.Lambda_star_etcContext):
        pass


    # Enter a parse tree produced by ExprParser#lambda_kwds.
    def enterLambda_kwds(self, ctx:ExprParser.Lambda_kwdsContext):
        pass

    # Exit a parse tree produced by ExprParser#lambda_kwds.
    def exitLambda_kwds(self, ctx:ExprParser.Lambda_kwdsContext):
        pass


    # Enter a parse tree produced by ExprParser#lambda_param_no_default.
    def enterLambda_param_no_default(self, ctx:ExprParser.Lambda_param_no_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#lambda_param_no_default.
    def exitLambda_param_no_default(self, ctx:ExprParser.Lambda_param_no_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#lambda_param_with_default.
    def enterLambda_param_with_default(self, ctx:ExprParser.Lambda_param_with_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#lambda_param_with_default.
    def exitLambda_param_with_default(self, ctx:ExprParser.Lambda_param_with_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#lambda_param_maybe_default.
    def enterLambda_param_maybe_default(self, ctx:ExprParser.Lambda_param_maybe_defaultContext):
        pass

    # Exit a parse tree produced by ExprParser#lambda_param_maybe_default.
    def exitLambda_param_maybe_default(self, ctx:ExprParser.Lambda_param_maybe_defaultContext):
        pass


    # Enter a parse tree produced by ExprParser#lambda_param.
    def enterLambda_param(self, ctx:ExprParser.Lambda_paramContext):
        pass

    # Exit a parse tree produced by ExprParser#lambda_param.
    def exitLambda_param(self, ctx:ExprParser.Lambda_paramContext):
        pass


    # Enter a parse tree produced by ExprParser#fstring_middle.
    def enterFstring_middle(self, ctx:ExprParser.Fstring_middleContext):
        pass

    # Exit a parse tree produced by ExprParser#fstring_middle.
    def exitFstring_middle(self, ctx:ExprParser.Fstring_middleContext):
        pass


    # Enter a parse tree produced by ExprParser#fstring_replacement_field.
    def enterFstring_replacement_field(self, ctx:ExprParser.Fstring_replacement_fieldContext):
        pass

    # Exit a parse tree produced by ExprParser#fstring_replacement_field.
    def exitFstring_replacement_field(self, ctx:ExprParser.Fstring_replacement_fieldContext):
        pass


    # Enter a parse tree produced by ExprParser#fstring_conversion.
    def enterFstring_conversion(self, ctx:ExprParser.Fstring_conversionContext):
        pass

    # Exit a parse tree produced by ExprParser#fstring_conversion.
    def exitFstring_conversion(self, ctx:ExprParser.Fstring_conversionContext):
        pass


    # Enter a parse tree produced by ExprParser#fstring_full_format_spec.
    def enterFstring_full_format_spec(self, ctx:ExprParser.Fstring_full_format_specContext):
        pass

    # Exit a parse tree produced by ExprParser#fstring_full_format_spec.
    def exitFstring_full_format_spec(self, ctx:ExprParser.Fstring_full_format_specContext):
        pass


    # Enter a parse tree produced by ExprParser#fstring_format_spec.
    def enterFstring_format_spec(self, ctx:ExprParser.Fstring_format_specContext):
        pass

    # Exit a parse tree produced by ExprParser#fstring_format_spec.
    def exitFstring_format_spec(self, ctx:ExprParser.Fstring_format_specContext):
        pass


    # Enter a parse tree produced by ExprParser#fstring.
    def enterFstring(self, ctx:ExprParser.FstringContext):
        pass

    # Exit a parse tree produced by ExprParser#fstring.
    def exitFstring(self, ctx:ExprParser.FstringContext):
        pass


    # Enter a parse tree produced by ExprParser#tstring_format_spec_replacement_field.
    def enterTstring_format_spec_replacement_field(self, ctx:ExprParser.Tstring_format_spec_replacement_fieldContext):
        pass

    # Exit a parse tree produced by ExprParser#tstring_format_spec_replacement_field.
    def exitTstring_format_spec_replacement_field(self, ctx:ExprParser.Tstring_format_spec_replacement_fieldContext):
        pass


    # Enter a parse tree produced by ExprParser#tstring_format_spec.
    def enterTstring_format_spec(self, ctx:ExprParser.Tstring_format_specContext):
        pass

    # Exit a parse tree produced by ExprParser#tstring_format_spec.
    def exitTstring_format_spec(self, ctx:ExprParser.Tstring_format_specContext):
        pass


    # Enter a parse tree produced by ExprParser#tstring_full_format_spec.
    def enterTstring_full_format_spec(self, ctx:ExprParser.Tstring_full_format_specContext):
        pass

    # Exit a parse tree produced by ExprParser#tstring_full_format_spec.
    def exitTstring_full_format_spec(self, ctx:ExprParser.Tstring_full_format_specContext):
        pass


    # Enter a parse tree produced by ExprParser#tstring_replacement_field.
    def enterTstring_replacement_field(self, ctx:ExprParser.Tstring_replacement_fieldContext):
        pass

    # Exit a parse tree produced by ExprParser#tstring_replacement_field.
    def exitTstring_replacement_field(self, ctx:ExprParser.Tstring_replacement_fieldContext):
        pass


    # Enter a parse tree produced by ExprParser#tstring_middle.
    def enterTstring_middle(self, ctx:ExprParser.Tstring_middleContext):
        pass

    # Exit a parse tree produced by ExprParser#tstring_middle.
    def exitTstring_middle(self, ctx:ExprParser.Tstring_middleContext):
        pass


    # Enter a parse tree produced by ExprParser#tstring.
    def enterTstring(self, ctx:ExprParser.TstringContext):
        pass

    # Exit a parse tree produced by ExprParser#tstring.
    def exitTstring(self, ctx:ExprParser.TstringContext):
        pass


    # Enter a parse tree produced by ExprParser#string.
    def enterString(self, ctx:ExprParser.StringContext):
        pass

    # Exit a parse tree produced by ExprParser#string.
    def exitString(self, ctx:ExprParser.StringContext):
        pass


    # Enter a parse tree produced by ExprParser#strings.
    def enterStrings(self, ctx:ExprParser.StringsContext):
        pass

    # Exit a parse tree produced by ExprParser#strings.
    def exitStrings(self, ctx:ExprParser.StringsContext):
        pass


    # Enter a parse tree produced by ExprParser#list.
    def enterList(self, ctx:ExprParser.ListContext):
        pass

    # Exit a parse tree produced by ExprParser#list.
    def exitList(self, ctx:ExprParser.ListContext):
        pass


    # Enter a parse tree produced by ExprParser#tuple.
    def enterTuple(self, ctx:ExprParser.TupleContext):
        pass

    # Exit a parse tree produced by ExprParser#tuple.
    def exitTuple(self, ctx:ExprParser.TupleContext):
        pass


    # Enter a parse tree produced by ExprParser#set.
    def enterSet(self, ctx:ExprParser.SetContext):
        pass

    # Exit a parse tree produced by ExprParser#set.
    def exitSet(self, ctx:ExprParser.SetContext):
        pass


    # Enter a parse tree produced by ExprParser#dict.
    def enterDict(self, ctx:ExprParser.DictContext):
        pass

    # Exit a parse tree produced by ExprParser#dict.
    def exitDict(self, ctx:ExprParser.DictContext):
        pass


    # Enter a parse tree produced by ExprParser#double_starred_kvpairs.
    def enterDouble_starred_kvpairs(self, ctx:ExprParser.Double_starred_kvpairsContext):
        pass

    # Exit a parse tree produced by ExprParser#double_starred_kvpairs.
    def exitDouble_starred_kvpairs(self, ctx:ExprParser.Double_starred_kvpairsContext):
        pass


    # Enter a parse tree produced by ExprParser#double_starred_kvpair.
    def enterDouble_starred_kvpair(self, ctx:ExprParser.Double_starred_kvpairContext):
        pass

    # Exit a parse tree produced by ExprParser#double_starred_kvpair.
    def exitDouble_starred_kvpair(self, ctx:ExprParser.Double_starred_kvpairContext):
        pass


    # Enter a parse tree produced by ExprParser#kvpair.
    def enterKvpair(self, ctx:ExprParser.KvpairContext):
        pass

    # Exit a parse tree produced by ExprParser#kvpair.
    def exitKvpair(self, ctx:ExprParser.KvpairContext):
        pass


    # Enter a parse tree produced by ExprParser#for_if_clauses.
    def enterFor_if_clauses(self, ctx:ExprParser.For_if_clausesContext):
        pass

    # Exit a parse tree produced by ExprParser#for_if_clauses.
    def exitFor_if_clauses(self, ctx:ExprParser.For_if_clausesContext):
        pass


    # Enter a parse tree produced by ExprParser#for_if_clause.
    def enterFor_if_clause(self, ctx:ExprParser.For_if_clauseContext):
        pass

    # Exit a parse tree produced by ExprParser#for_if_clause.
    def exitFor_if_clause(self, ctx:ExprParser.For_if_clauseContext):
        pass


    # Enter a parse tree produced by ExprParser#listcomp.
    def enterListcomp(self, ctx:ExprParser.ListcompContext):
        pass

    # Exit a parse tree produced by ExprParser#listcomp.
    def exitListcomp(self, ctx:ExprParser.ListcompContext):
        pass


    # Enter a parse tree produced by ExprParser#setcomp.
    def enterSetcomp(self, ctx:ExprParser.SetcompContext):
        pass

    # Exit a parse tree produced by ExprParser#setcomp.
    def exitSetcomp(self, ctx:ExprParser.SetcompContext):
        pass


    # Enter a parse tree produced by ExprParser#genexp.
    def enterGenexp(self, ctx:ExprParser.GenexpContext):
        pass

    # Exit a parse tree produced by ExprParser#genexp.
    def exitGenexp(self, ctx:ExprParser.GenexpContext):
        pass


    # Enter a parse tree produced by ExprParser#dictcomp.
    def enterDictcomp(self, ctx:ExprParser.DictcompContext):
        pass

    # Exit a parse tree produced by ExprParser#dictcomp.
    def exitDictcomp(self, ctx:ExprParser.DictcompContext):
        pass


    # Enter a parse tree produced by ExprParser#arguments.
    def enterArguments(self, ctx:ExprParser.ArgumentsContext):
        pass

    # Exit a parse tree produced by ExprParser#arguments.
    def exitArguments(self, ctx:ExprParser.ArgumentsContext):
        pass


    # Enter a parse tree produced by ExprParser#args.
    def enterArgs(self, ctx:ExprParser.ArgsContext):
        pass

    # Exit a parse tree produced by ExprParser#args.
    def exitArgs(self, ctx:ExprParser.ArgsContext):
        pass


    # Enter a parse tree produced by ExprParser#kwargs.
    def enterKwargs(self, ctx:ExprParser.KwargsContext):
        pass

    # Exit a parse tree produced by ExprParser#kwargs.
    def exitKwargs(self, ctx:ExprParser.KwargsContext):
        pass


    # Enter a parse tree produced by ExprParser#starred_expression.
    def enterStarred_expression(self, ctx:ExprParser.Starred_expressionContext):
        pass

    # Exit a parse tree produced by ExprParser#starred_expression.
    def exitStarred_expression(self, ctx:ExprParser.Starred_expressionContext):
        pass


    # Enter a parse tree produced by ExprParser#kwarg_or_starred.
    def enterKwarg_or_starred(self, ctx:ExprParser.Kwarg_or_starredContext):
        pass

    # Exit a parse tree produced by ExprParser#kwarg_or_starred.
    def exitKwarg_or_starred(self, ctx:ExprParser.Kwarg_or_starredContext):
        pass


    # Enter a parse tree produced by ExprParser#kwarg_or_double_starred.
    def enterKwarg_or_double_starred(self, ctx:ExprParser.Kwarg_or_double_starredContext):
        pass

    # Exit a parse tree produced by ExprParser#kwarg_or_double_starred.
    def exitKwarg_or_double_starred(self, ctx:ExprParser.Kwarg_or_double_starredContext):
        pass


    # Enter a parse tree produced by ExprParser#star_targets.
    def enterStar_targets(self, ctx:ExprParser.Star_targetsContext):
        pass

    # Exit a parse tree produced by ExprParser#star_targets.
    def exitStar_targets(self, ctx:ExprParser.Star_targetsContext):
        pass


    # Enter a parse tree produced by ExprParser#star_targets_list_seq.
    def enterStar_targets_list_seq(self, ctx:ExprParser.Star_targets_list_seqContext):
        pass

    # Exit a parse tree produced by ExprParser#star_targets_list_seq.
    def exitStar_targets_list_seq(self, ctx:ExprParser.Star_targets_list_seqContext):
        pass


    # Enter a parse tree produced by ExprParser#star_targets_tuple_seq.
    def enterStar_targets_tuple_seq(self, ctx:ExprParser.Star_targets_tuple_seqContext):
        pass

    # Exit a parse tree produced by ExprParser#star_targets_tuple_seq.
    def exitStar_targets_tuple_seq(self, ctx:ExprParser.Star_targets_tuple_seqContext):
        pass


    # Enter a parse tree produced by ExprParser#star_target.
    def enterStar_target(self, ctx:ExprParser.Star_targetContext):
        pass

    # Exit a parse tree produced by ExprParser#star_target.
    def exitStar_target(self, ctx:ExprParser.Star_targetContext):
        pass


    # Enter a parse tree produced by ExprParser#target_with_star_atom.
    def enterTarget_with_star_atom(self, ctx:ExprParser.Target_with_star_atomContext):
        pass

    # Exit a parse tree produced by ExprParser#target_with_star_atom.
    def exitTarget_with_star_atom(self, ctx:ExprParser.Target_with_star_atomContext):
        pass


    # Enter a parse tree produced by ExprParser#star_atom.
    def enterStar_atom(self, ctx:ExprParser.Star_atomContext):
        pass

    # Exit a parse tree produced by ExprParser#star_atom.
    def exitStar_atom(self, ctx:ExprParser.Star_atomContext):
        pass


    # Enter a parse tree produced by ExprParser#single_target.
    def enterSingle_target(self, ctx:ExprParser.Single_targetContext):
        pass

    # Exit a parse tree produced by ExprParser#single_target.
    def exitSingle_target(self, ctx:ExprParser.Single_targetContext):
        pass


    # Enter a parse tree produced by ExprParser#single_subscript_attribute_target.
    def enterSingle_subscript_attribute_target(self, ctx:ExprParser.Single_subscript_attribute_targetContext):
        pass

    # Exit a parse tree produced by ExprParser#single_subscript_attribute_target.
    def exitSingle_subscript_attribute_target(self, ctx:ExprParser.Single_subscript_attribute_targetContext):
        pass


    # Enter a parse tree produced by ExprParser#t_primary.
    def enterT_primary(self, ctx:ExprParser.T_primaryContext):
        pass

    # Exit a parse tree produced by ExprParser#t_primary.
    def exitT_primary(self, ctx:ExprParser.T_primaryContext):
        pass


    # Enter a parse tree produced by ExprParser#t_lookahead.
    def enterT_lookahead(self, ctx:ExprParser.T_lookaheadContext):
        pass

    # Exit a parse tree produced by ExprParser#t_lookahead.
    def exitT_lookahead(self, ctx:ExprParser.T_lookaheadContext):
        pass


    # Enter a parse tree produced by ExprParser#del_targets.
    def enterDel_targets(self, ctx:ExprParser.Del_targetsContext):
        pass

    # Exit a parse tree produced by ExprParser#del_targets.
    def exitDel_targets(self, ctx:ExprParser.Del_targetsContext):
        pass


    # Enter a parse tree produced by ExprParser#del_target.
    def enterDel_target(self, ctx:ExprParser.Del_targetContext):
        pass

    # Exit a parse tree produced by ExprParser#del_target.
    def exitDel_target(self, ctx:ExprParser.Del_targetContext):
        pass


    # Enter a parse tree produced by ExprParser#del_t_atom.
    def enterDel_t_atom(self, ctx:ExprParser.Del_t_atomContext):
        pass

    # Exit a parse tree produced by ExprParser#del_t_atom.
    def exitDel_t_atom(self, ctx:ExprParser.Del_t_atomContext):
        pass


    # Enter a parse tree produced by ExprParser#type_expressions.
    def enterType_expressions(self, ctx:ExprParser.Type_expressionsContext):
        pass

    # Exit a parse tree produced by ExprParser#type_expressions.
    def exitType_expressions(self, ctx:ExprParser.Type_expressionsContext):
        pass


    # Enter a parse tree produced by ExprParser#func_type_comment.
    def enterFunc_type_comment(self, ctx:ExprParser.Func_type_commentContext):
        pass

    # Exit a parse tree produced by ExprParser#func_type_comment.
    def exitFunc_type_comment(self, ctx:ExprParser.Func_type_commentContext):
        pass



del ExprParser